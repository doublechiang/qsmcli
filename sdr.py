#!/usr/bin/env python3

import os, sys
import subprocess
from globalvars import GlobalVars

class Sdr:

    @staticmethod
    def supported_cmds():
        return ['info', 'list', 'elist']

    def sdr_info():
        cmdline = GlobalVars.host_access() + " sdr info"
        print(cmdline)
        osstdout = subprocess.check_call(cmdline.split())

    def sdr_list():
        cmdline = GlobalVars.host_access() + " sdr list"
        osstdout = subprocess.check_call(cmdline.split())

    def sdr_elist():
        cmdline = GlobalVars.host_access() + " sdr elist"
        osstdout = subprocess.check_call(cmdline.split())

    def sdr():
        cmdline = GlobalVars.host_access() + " sdr"
        osstdout = subprocess.check_call(cmdline.split())

    def __init__(self, arg):
        switcher = {
            "info": self.sdr_info,
            "list": self.sdr_list,
            "elist": self.sdr_elist,
            "": self.sdr
            }
        switcher[arg]()
        return None
