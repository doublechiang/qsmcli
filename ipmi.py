#!/usr/bin/env python3

import os, sys

from globalvars import GlobalVars
from exec import Exec

class Ipmi():
    def __init__(self, arg):
        self.ipmi_redirect(arg)

    def ipmi_redirect(self, arg):
        cmdline = GlobalVars.host_access() + " " + arg
        Exec(cmdline)
