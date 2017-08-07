#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Mac():
    """ send several raw mac command and print out the mac we got
    """

    @staticmethod
    def supported_cmds():
        return []


    def getSystemMac(self):
        cmdline = GlobalVars.host_access() + " raw 0x0c 0x01 0x01 0xff 0x00"
        output= Exec(cmdline)


    def __init__(self, arg):
        switcher = {
            }
        switcher[arg]()
        return None
