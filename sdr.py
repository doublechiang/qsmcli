#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Sdr:

    @staticmethod
    def supported_cmds():
        return ['info', 'list', 'elist']

    def sdr_info(self):
        cmdline = GlobalVars.host_access() + " sdr info"
        Exec(cmdline)

    def sdr_list(self):
        cmdline = GlobalVars.host_access() + " sdr list"
        Exec(cmdline)

    def sdr_elist(self):
        cmdline = GlobalVars.host_access() + " sdr elist"
        Exec(cmdline)

    def sdr(self):
        cmdline = GlobalVars.host_access() + " sdr"
        Exec(cmdline)

    def __init__(self, arg):
        switcher = {
            "info": self.sdr_info,
            "list": self.sdr_list,
            "elist": self.sdr_elist,
            "": self.sdr
            }
        switcher[arg]()
        return None
