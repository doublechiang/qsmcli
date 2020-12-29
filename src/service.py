#!/usr/bin/env python3

import os, sys
import logging
import subcmd
import inspect
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg
from devmgr import DevMgr

class Service(subcmd.SubCmd):
    """
    eanble/disable Service commands:
    service [web|kvm|cd-media|hd-media|ssh|solssh] [enable/disable]
    Plesae notice this utility will get the service configuation data and then
    based on the configuration get then set the whole configuration.
     It do not guarantee that BMC has this feature.
    """

    get_conf = [0x32, 0x69]
    set_conf = [0x32, 0x6a]

    supported_services = {
        "web": [1, 0, 0, 0],
        "kvm": [2, 0, 0, 0],
        "cd-media": [4, 0, 0, 0],
        "hd-media": [0x10, 0, 0, 0],
        "ssh": [0x20, 0, 0, 0],
        "solssh": [0x80, 0, 0, 0]
    }

    svcAction = {
        "disable": [0],
        "enable": [1]
    }

    def subService(self, arg):
        """ All services commands required to send the get configuration then set the configuration.
        """
        logging.info('%s, arg=%s', inspect.currentframe().f_code.co_filename, arg)
        target = arg.split()[0]
        action = arg.split()[1]
        getraw = self.composeList(Service.get_conf, Service.supported_services[target])
        msg = IpmiMsg(getraw)
        response_hex = IpmiExec().run(msg).output().split()
        response = [int(x,16) for x in response_hex]

        # Grantley platform, at least S2B, check S2B for further trailing zero.
        devid = DevMgr().getId()
        if devid == DevMgr.DEVID_S2B:
            setmsg = IpmiMsg(self.composeList(Service.set_conf, Service.supported_services[target], Service.svcAction[action], response[5:34], [0,0,0]))
        else:
            setmsg = IpmiMsg(self.composeList(Service.set_conf, Service.supported_services[target], Service.svcAction[action], response[5:34], [0,0]))

        IpmiExec().run(setmsg)


    def __init__(self, arg=None):
        self.subs = {
            "web": self.subService,
            "kvm": self.subService,
            "cd-media": self.subService,
            "hd-media": self.subService,
            "ssh": self.subService,
            "solssh": self.subService
        }
