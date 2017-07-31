#!/usr/bin/env python3

import os, sys
import subprocess

from globalvars import GlobalVars

class Ipmi():
    def __init__(self, arg):
        Ipmi.ipmi_redirect(arg)

    @staticmethod
    def ipmi_redirect(arg):
        cmdline = GlobalVars.host_access() + " " + arg
        print(cmdline)
#        osstdout = subprocess.check_call(cmdline.split())
