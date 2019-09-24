#!/usr/bin/env python3

import os, sys
import subprocess

from globalvars import GlobalVars
from ipmiexec import IpmiExec

class Ipmi():
    """ ipmitool command
    redirect parameters suffix to ipmitool
    """

    def __init__(self, arg):
        self.ipmi_redirect(arg)

    def ipmi_redirect(self, arg):
        IpmiExec(arg).run(printcmd=True)
