#!/usr/bin/env python3

import os, sys
import subprocess

from ipmiexec import IpmiExec

class Ipmi():
    """ ipmitool command
        redirect parameters suffix to ipmitool
    """

    def run(self, arg):
        IpmiExec().run(arg, printcmd=True)
