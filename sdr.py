#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Sdr:
    """Sensor Data Record command
    info: print the information
    list: list the sdr
    elist: elist the
    """

    @staticmethod
    def supported_cmds():
        return ['info', 'list', 'elist']

    def sdr_info(self):
        cmdline = GlobalVars.host_access() + " sdr info"
        Exec(cmdline, printcmd=True)

    def sdr_list(self):
        cmdline = GlobalVars.host_access() + " sdr list"
        Exec(cmdline, printcmd=True)

    def sdr_elist(self):
        cmdline = GlobalVars.host_access() + " sdr elist"
        Exec(cmdline, printcmd=True)

    def sdr(self):
        cmdline = GlobalVars.host_access() + " sdr"
        Exec(cmdline, printcmd=True)

    def not_supported(self):
        print("Not supported commands")
        print(Sdr.__doc__)

    def __init__(self, arg):
        switcher = {
            "info": self.sdr_info,
            "list": self.sdr_list,
            "elist": self.sdr_elist,
            "": self.sdr
            }
        func =  switcher.get(arg, self.not_supported)
        func()

        return
