#!/usr/bin/env python3

import os, sys
import subprocess

from globalvars import GlobalVars


class IpmiExec():
    """ IPM command Object.
    """

    def __init__(self, arg=None):
        self.arg = arg

    def output(self):
        return self.stdout

    def run(self, arg=None, printcmd=None):
        try:
            cmd = GlobalVars.host_access() + self.arg
            if (printcmd):
                print(cmd)
            completed = subprocess.run(cmd.split(), universal_newlines = True, stdout=subprocess.PIPE)
#            print(completed.stdout.split())
            self.stdout=completed.stdout
            if (printcmd):
                print(self.stdout)
        except:
            print("Exception generated!")
        return self


    def marshal_raw_cmds(self, *argv):
        """ Assemble the raw commands of get configuration.
            parameter argv: every arguments is a list with value for raw commands.
        """

        cmdbuf = ""
        #every argument is a digit list
        for list in argv:
            for val in list:
                cmdbuf += "0x%x " % val

        rawcmd = " raw " + cmdbuf
        self.arg = rawcmd
        return self

    def with_bridge(self, bridge):
        self.arg = "-t " + str(bridge) + " " + self.arg
        return self

    def with_channel(self, channel):
        self.arg = "-b " + str(channel) + " " + self.arg
        return self
