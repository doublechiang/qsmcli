#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Nic():
    """ nic command: get, set the NIC dedicate/share NIC
    nic dedicate
    nic lom-share
    nic mezz-share0
    nic mizz-share1
    nic: print the supported sub commands.

    Return: <complete code> <LAN Card Type>
    For LAN Card Type,
    0h- BMC Dedicated
    2h- Shared NIC (OCP Mezzanine slot)
    3h- Shared NIC (QCT Mezzanine slot)
    """

    @staticmethod
    def supported_cmds():
        return ['dedicate', 'lom-share', 'mezz-share0', 'mezz-share1']

    def dedicate(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x00"
        Exec(cmdline, printcmd=True)

    def lom_share(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x01"
        Exec(cmdline, printcmd=True)

    def mezz_share0(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x02"
        Exec(cmdline, printcmd=True)

    def mezz_share1(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x03"
        Exec(cmdline)

    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (Nic.__doc__)
            return

        switcher = {
            "dedicate": self.dedicate,
            "lom-share": self.lom_share,
            "mezz-share0": self.mezz_share0,
            "mezz-sahre1": self.mezz_share1,
            }
        func =  switcher.get(arg, print(Nic.__doc__))
        func()
        return None
