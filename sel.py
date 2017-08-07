#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Sel:

    @staticmethod
    def supported_cmds():
        return ['info', 'list']

    def sel_info(self):
        cmdline = GlobalVars.host_access() + " sel info"
        Exec(cmdline)

    def sel_list(self):
        cmdline = GlobalVars.host_access() + " sel list"
        Exec(cmdline)

    def sel(self):
        cmdline = GlobalVars.host_access() + " sel list"
        Exec(cmdline)

    def __init__(self, arg):
        switcher = {
            "info": self.sel_info,
            "list": self.sel_list,
            "": self.sel
            }
        switcher[arg]()
        return None
