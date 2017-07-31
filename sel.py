#!/usr/bin/env python3

import os, sys
import subprocess
from globalvars import GlobalVars

class Sel:

    @staticmethod
    def supported_cmds():
        return ['info', 'list']

    def sel_info(self):
        cmdline = GlobalVars.host_access() + " sel info"
        print(cmdline)
#        osstdout = subprocess.check_call(cmdline.split())

    def sel_list(self):
        cmdline = GlobalVars.host_access() + " sel list"
        print(cmdline)
#        osstdout = subprocess.check_call(cmdline.split())

    def sel(self):
        cmdline = GlobalVars.host_access() + " sel list"
        print(cmdline)
#        osstdout = subprocess.check_call(cmdline.split())

    def __init__(self, arg):
        switcher = {
            "info": self.sel_info,
            "list": self.sel_list,
            "": self.sel
            }
        switcher[arg]()
        return None
