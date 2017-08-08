#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Mac():
    """ send raw get system mac command and print out the system mac we have
    mac [index], index range from 0 to 5
    for example: mac 0
    """
    @staticmethod
    def supported_cmds():
        return ['0', '1', '2', '3', '4', '5']

    def print_ieee(self, arg):
        for token in arg[:-1]:
                print(token, end='')
                print(':', end='')
        print(arg[-1])

    def parse_raw_response(self, arg):
        """ Return the mac address string format
        """
        token=arg
        if token[0] == "ff":
            print("Mac addresss not presented.")
        else:
            self.print_ieee(token[2:8])

    def getSystemMac(self, arg):
        cmdline = GlobalVars.host_access() + " raw 0x030 0x019 " + arg + " 0x00"
        result= Exec(cmdline)
        self.parse_raw_response(result.stdout.split())

    def not_supported(self):
        print("Not supported commands")
        print(Mac.__doc__)

    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (Mac.__doc__)
            return
        try:
            val = int(arg)
            if (val >= 0) and (val < 6):
                self.getSystemMac(arg)
            else:
                self.not_supported()
        except:
            self.not_supported()


        return
