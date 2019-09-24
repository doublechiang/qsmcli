#!/usr/bin/env python3

import os, sys
import subprocess

class Exec():
    """ Executing the command the arguement """

    def __init__(self, arg=None, printcmd=None):
        if printcmd:
            print(arg)
        try:
#            completed = subprocess.run(arg.split(), stdout=subprocess.PIPE)
            completed = subprocess.run(arg.split(), universal_newlines = True, stdout=subprocess.PIPE)
#            print(completed.stdout.split())
            self.stdout=completed.stdout
            if printcmd:
                print(self.stdout)
        except:
            print("Exception generated!")

    def output(self):
        return self.stdout

    def run(self, arg):
        pass


    def marshal_raw_cmds(self, *argv):
        """ Assemble the raw commands of get configuration.
            parameter argv: every arguments is a list with value for raw commands.
        """

        self.cmdbuf = ""
        #every argument is a digit list
        for list in argv:
            for val in list:
                self.cmdbuf += "0x%x " % val

        self.cmdbuf = " raw " + self.cmdbuf
        return self.cmdbuf
