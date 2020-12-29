#!/usr/bin/env python3

import os, sys
import logging
import inspect
import requests
import json
import time
import urllib3


import subcmd
from ipmimsg import IpmiMsg
from ipmiexec import IpmiExec
from config import Config
from devmgr import DevMgr


class Fw(subcmd.SubCmd):
    """ fw commands: Firmware maintence, for BIOS and BMC upgrade through http interface.
        supported platform: Purley S5B
    fw update [bios|bmc] [image]
    description: upgrade the supplied image file through web interface.
    """
    CATEGORY = ["bios", "bmc"]
    BMC_COMPLETED='Completed.'
    
    def update(self, arg):
        """ Update commands.
        """
        logging.info('%s, arg=%s', inspect.currentframe().f_code.co_filename, arg)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        grpid = DevMgr().getGrp()
        if grpid != 'S5x':
            logging.error("Update through Web Interface currently only support S5x")
            return

        try:
            currentdir = os.getcwd()
            target, fn = self.__parse_arg(arg)
        except ValueError:
            print(self.__doc__)
            return

        # Get the host and credentials.
        env=Config().current
        env['fn']= fn

        if target == 'bios':
            self.__update_bios(env)
        elif target == 'bmc':
            self.__update_bmc(env)

    def __get_cookie_csrf(self, env):
        url = 'https://' + env.get('host') + '/api/session'
        response = requests.post(url, 
                data={'password': env.get('passw'), 'username': env.get('user')}, 
                headers={'Content-Type': 'application/x-www-form-urlencoded'}, 
                        verify=False)
        if response.status_code != 200:
            raise RuntimeError("Error get the session object")

        csrftoken=json.loads(response.content)['CSRFToken']
        cookie=response.headers['Set-Cookie']
        return (cookie, csrftoken)

    def __update_bios(self, env):
        cookie, csrftoken = self.__get_cookie_csrf(Config().current)

        with requests.Session() as session:

                # init the bios flash
                session.headers.update({'Cookie': cookie, 'X-CSRFTOKEN': csrftoken})
                session.verify=False
                url = 'https://' + env.get('host') + '/api/maintenance/biosflash'
                response=session.put(url)
                if response.status_code != 200:
                        raise RuntimeError("Can't create session")

                # upload bios file
                files = {'fwimage': open(env.get('fn'),'rb')}
                print("Uploading image....")
                url = 'https://' + env.get('host') + '/api/maintenance/bios'

                response=session.post(url, files=files)
                if response.status_code != 200:
                        raise RuntimeError("Uploadb image failed")

                # Verification BIOS
                url = 'https://' + env.get('host') + '/api/maintenance/bios/verification'
                response=session.get(url)
                if response.status_code != 200:
                        raise RuntimeError("Verifying BIOS image failed")

                # Upgrade BIOS
                url = 'https://' + env.get('host') + '/api/maintenance/bios/upgrade'
                response=session.put(url)
                if response.status_code != 200:
                        raise RuntimeError("Upgrade BIOS failed.")

                # Get Progress
                progress = 0
                duration= 0
                url = 'https://' + env.get('host') + '/api/maintenance/bios/flash-progress'
                while progress != 100:
                        interval =10
                        response=session.get(url)
                        if response.status_code != 200:
                                raise RuntimeError("Can't get flash progress")
                        print(response.content)
                        progress=int(json.loads(response.content)['percentage'])
                        print("Progress {}%".format(progress))

                        time.sleep(interval)
                        duration+=interval
                        if (duration > 300):
                                raise TimeoutError

                # Progress complete
                url = 'https://' + env.get('host') + '/api/maintenance/bios/flash-done'
                session.put(url, 
                        headers={'Content-Type': 'application/json', 'Content-Length': '0'})

                # delete session
                session.delete('https://' + env.get('host') + '/api/session')


    def __update_bmc(self, env):
        cookie, csrftoken = self.__get_cookie_csrf(Config().current)

        with requests.Session() as session:

                # init the bios flash
                session.headers.update({'Cookie': cookie, 'X-CSRFTOKEN': csrftoken})
                session.verify=False
                response=session.put('https://' + env.get('host') + '/api/maintenance/flash',
                            headers={'Content-Type': 'application/json;'})
                if response.status_code != 200:
                        raise RuntimeError("Can't create session")

                # upload BMC image
                files = {'fwimage': open(env.get('fn'),'rb')}
                print("Uploading image....")
                url = 'https://' + env.get('host') + '/api/maintenance/firmware'

                response=session.post(url, files=files)
                if response.status_code != 200:
                        raise RuntimeError("Upload image failed")

                # Verification BMC
                response=session.get('https://' + env.get('host') + '/api/maintenance/firmware/verification')
                if response.status_code != 200:
                        raise RuntimeError("Verifying BMC image failed")

                # Upgrade BMC
                response=session.put('https://' + env.get('host') + '/api/maintenance/firmware/upgrade',
                        headers={'Content-Type':'Application/json;'},
                        data="{'preserve_config':0,'flash_status':1}")
                if response.status_code != 200:
                        raise RuntimeError("Upgrade BMC image failed.")

                # Get Progress
                progress = 0
                duration= 0
                url = 'https://' + env.get('host') + '/api/maintenance/firmware/flash-progress'
                while progress != Fw.BMC_COMPLETED:
                        interval =5
                        response=session.get(url)
                        if response.status_code != 200:
                                raise RuntimeError("Can't get flash progress")
                        logging.info(json.loads(response.content))
                        progress=json.loads(response.content).get('progress')
                        if progress:
                                print("Progress {}".format(progress))
                                if progress != Fw.BMC_COMPLETED:
                                        time.sleep(interval)
                                        duration+=interval
                                        if (duration > 300):
                                                raise TimeoutError
                        else:
                                raise RuntimeError("retured progress can't be parsed")

                # Progress complete
                session.put('https://' + env.get('host') + '/api/maintenance/firmware/flash-done')

                # reset BMC
                session.post('https://' + env.get('host') + '/api/maintenance/reset',
                        headers={'Content-Type': 'application/json', 'Content-Length': '0'})
                print("Resetting BMC, please wait 90 seconds for BMC to boot.")

                

    def __parse_arg(self, arg):
        token=arg.split()
        if len(token) != 3:
            raise ValueError
        # support if type is in the list
        target = token[1]
        if target not in Fw.CATEGORY:
            raise ValueError
        # check if image file exist
        fn = token[2]
        if not os.path.isfile(fn):
            print("can't find file {}".format(fn))
            raise ValueError
        return (target, fn)


    def __init__(self):
        self.subs = { 'update': self.update }
