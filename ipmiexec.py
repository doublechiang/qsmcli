#!/usr/bin/env python3

import os, sys
import subprocess
import logging
import sub_command
from globalvars import GlobalVars
from ipmimsg import IpmiMsg

class IpmiExec():
    """ IPMI command Helper laye to execute the commands
    """

    def output(self):
        return self.stdout

    def run(self, msg:IpmiMsg, printcmd=True):
        logging.info("Ipmiexec.run() is called, msgobj=%s", msg)
        # if there is no existing command, we will composing one
        cmd = GlobalVars.host_access() + msg.format()
        if (printcmd):
            print(cmd)
        completed = subprocess.run(cmd.split(), universal_newlines = True, stdout=subprocess.PIPE)
        # print(completed.stdout.split())
        self.stdout=completed.stdout
        if (printcmd):
            print(self.stdout)

        return self
