#!/usr/bin/env python3

import os, sys
import logging
import subcmd
from ipmiexec import IpmiExec

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

    enable_service = [1]
    disable_service = [0]

    supported_cmds = [ 'web', 'kvm', 'cd-media', 'hd-media', 'ssh', 'solssh' ]

    valid_cmd = { 'web': ['enable', 'disable'], 
        'kvm': ['enable', 'disable'],
        'cd-media': ['enable', 'disable'],
        'hd-media': ['enable', 'disable'],
        'ssh': ['enable', 'disable'],
        'solssh': ['enable', 'disable']
    }


    def setUp(self, ipmiexec):
        """ For service commands, need to issue get config commands first
        """
        logging.info("%s is called, self.arg=%s", self.setUp, self.arg)
        target = self.arg.split()[0]
        action = self.arg.split()[1]
        exec = IpmiExec().marshal_raw_cmds(Service.get_conf, Service.supported_services[target]).composite_cmds().run()
        response_hex = exec.output().split()
        response = [int(x,16) for x in response_hex]

        actionCmd = {
            "enable": Service.enable_service,
            "disable": Service.disable_service
        }

        ipmiexec.marshal_raw_cmds([int(x,16) for x in ipmiexec.raw.split()], actionCmd[action], response[5:34], [0,0])
        
    def __join_list(self, *argv ):
        logging.debug(argv)
        retlist= []
        for list in argv:
            retlist += list
        return retlist

    def __validate_arg(self, arg):
        """ Return true if the argument is correct
        """
        logging.debug("arg=%s", arg)
        if arg == None:
            return False

        token = arg.split()
        try:
            if (len(token) >= 1):
                if not (token[0] in self.valid_cmd):
                    raise ValueError
                if len(token) >= 2:
                    allowed_list = self.valid_cmd[token[0]]
                    if not (token[1] in allowed_list):
                        raise ValueError
                else:
                # In this commands, every command should follow with enable/disable
                    raise ValueError
        except:
            self.not_supported()
            return False
        return True


    def __init__(self, arg=None):
        super().__init__(arg)
        self.cmds = dict()
        if self.__validate_arg(arg):
            self.cmds = {
                "web": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['web']),
                "kvm": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['kvm']),
                "cd-media": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['cd-media']),
                "hd-media": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['hd-media']),
                "ssh": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['ssh']),
                "solssh": IpmiExec(setup=self.setUp).marshal_raw_cmds(Service.set_conf, Service.supported_services['solssh'])
            }
