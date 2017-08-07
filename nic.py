#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Nic():

    @staticmethod
    def supported_cmds():
        return ['dedicate', 'lom-share', 'mezz-share0', 'mezz-share1']

    def dedicate(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x00"
        Exec(cmdline)

    def lom_share(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x01"
        Exec(cmdline)

    def mezz_share0(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x02"
        Exec(cmdline)

    def mezz_share1(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x03"
        Exec(cmdline)

    def nic(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x02 0x01 0xff 0x0 0x0"
        Exec(cmdline)

    def __init__(self, arg):
        switcher = {
            "dedicate": self.dedicate,
            "lom-share": self.lom_share,
            "mezz-share0": self.mezz_share0,
            "mezz-sahre1": self.mezz_share1,
            "": self.sel
            }
        switcher[arg]()
        return None
