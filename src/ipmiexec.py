#!/usr/bin/env python3

import os, sys
import subprocess
import logging
import subcmd

# local modules definition below
from interface import Interface
from ipmimsg import IpmiMsg
from config import Config

class IpmiExec():
    """ IPMI command Helper laye to execute the commands
    """

    def output(self):
        return self.stdout

    def run(self, msg:IpmiMsg, printcmd=True):
        """ hostenv is a dictionary contain host ip & username/password
        """
        logging.info("Ipmiexec.run() is called, msgobj=%s", msg)
        ntrfce = Interface(**Config().current)

        # if there is no existing command, we will composing one
        cmd = "ipmitool {}{}".format(ntrfce.format(), msg.format())
        if (printcmd):
            print(cmd)
        completed = subprocess.run(cmd.split(), universal_newlines = True, stdout=subprocess.PIPE)
        # print(completed.stdout.split())
        self.stdout=completed.stdout
        if (printcmd):
            print(self.stdout)

        return self


