#!/usr/bin/env python3

import os, sys
import subprocess

class Exec():
    """ Executing the command the arguement """

    def __init__(self, arg):
        print(arg)
        osstdout = subprocess.check_call(arg.split())
        return
