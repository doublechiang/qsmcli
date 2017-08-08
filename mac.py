#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Mac():
    """ send several raw mac command and print out the mac we got
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


    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (Mac.__doc__)
            return

        self.getSystemMac(arg)
        return
