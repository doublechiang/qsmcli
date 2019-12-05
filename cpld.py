    #!/usr/bin/env python3

import os, sys
import logging
from globalvars import GlobalVars
from ipmiexec import IpmiExec
from sub_command import SubCommand

class Cpld(SubCommand):
    """
    get CPLD information:
    cpld [fw|cksum|id]
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    cpld_fw = [0x30, 0x17, 3]
    cpld_cksum = [0x30, 0x17, 1]
    cpld_id = [0x30, 0x17, 2]

    supported_cmds = ['fw', 'cksum', 'id']

    def __validate_arg(self, arg):
        try:
            if arg is None or len(arg.split()) == 0:
                raise ValueError

            if len(arg.split()) > 0:
                if not arg.split()[0] in self.cmds:
                    raise ValueError
        except ValueError:
            self.not_supported()
            return False

        return True


    def __init__(self, arg=None):
        super().__init__(arg)
        self.cmds = {
            "fw" : IpmiExec().marshal_raw_cmds(Cpld.cpld_fw),
            "cksum" : IpmiExec().marshal_raw_cmds(Cpld.cpld_cksum),
            "id" : IpmiExec().marshal_raw_cmds(Cpld.cpld_id)
        }
        self.__validate_arg(arg)
