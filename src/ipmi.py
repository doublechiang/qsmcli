#!/usr/bin/env python3

import os, sys
import subprocess

import subcmd
from ipmiexec import IpmiExec

class Ipmi(subcmd.SubCmd):
    """ ipmitool command
        redirect parameters suffix to ipmitool
    """
    def do_run(self, arg):
        IpmiExec().run(arg, printcmd=True)


    def __init__(self, arg=None):
        # No more sub commands, so return the function directly
        self.subs = self.do_run
