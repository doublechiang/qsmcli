#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from sub_command import SubCommand
from ipmiexec import IpmiExec

class Service(SubCommand):
    """ Service commands:
    service enable/disable [services]
    [service] include web, kvm, cd-media, hd-media, ssh and solssh.
    Plesae notice this utility will get the service configuation data and
    set the configuation data when set it. It do not guarantee that BMC has this feature.

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

    @staticmethod
    def supported_cmds():
        return ['enable', 'disable']

    def enable(self, arg):
        # check if the service is in the supported serivce
        if not self.__validate_service_arg(arg):
            return

        # get the service configutaion.
        service = self.supported_services[arg[0]]
        exec=IpmiExec()
        raw_cmds = exec.marshal_raw_cmds(self.get_conf, service).run(printcmd=True)
        response_hex = exec.output().split()
        response = [int(x,16) for x in response_hex]

        exec.marshal_raw_cmds(self.set_conf, service, Service.enable_service, response[5:34], [0, 0]).run(printcmd=True)


    def disable(self, arg):
        if not self.__validate_service_arg(arg):
            return
        # get the service configutaion.
        service = self.supported_services[arg[0]]
        exec = IpmiExec()
        raw_cmds = exec.marshal_raw_cmds(self.get_conf, service).run(printcmd=True)
        response_hex = exec.output().split()
        response = [int(x,16) for x in response_hex]

        raw_cmds = exec.marshal_raw_cmds(self.set_conf, service, Service.disable_service, response[5:34], [0, 0]).run(printcmd=True)


    def __validate_service_arg(self, arg):
        try:
            if len(arg) != 1:
                raise ValueError

            if not (arg[0] in self.supported_services):
                raise ValueError
        except:
            self.not_supported()
            return False
        return True


    def __init__(self, arg):

        # enable/disable [service], argument must be 2
        arglist = arg.split()
        if len(arglist) != 2:
            self.not_supported()
            return

        switcher = {
            "enable": self.enable,
            "disable": self.disable,
            }
        func =  switcher.get(arglist[0], self.not_supported)
        func(arglist[1:])
        return
