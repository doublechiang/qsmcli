#!/usr/bin/env python3

import os, sys
import subprocess

class Exec():
    """ Executing the command the arguement """

    def __init__(self, arg, printcmd=None):
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
