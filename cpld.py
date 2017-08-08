#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Cpld():
    """ CPLD sub commands:
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    @staticmethod
    def supported_cmds():
        return ['fw', 'cksum', 'id']

    def fw(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x03"
        Exec(cmdline, printcmd=True)

    def cksum(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x01"
        Exec(cmdline, printcmd=True)

    def id(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x02"
        Exec(cmdline, printcmd=True)

    def not_supported(self):
        print("Not supported commands")
        print(Cpld.__doc__)


    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (Cpld.__doc__)
            return

        switcher = {
            "fw": self.fw,
            "cksum": self.cksum,
            "id": self.id,
            }
        func =  switcher.get(arg, self.not_supported)
        func()
