#!/usr/bin/env python3

import os, sys
import logging
import inspect


from nic import Nic
from mac import Mac
from cpld import Cpld
from fan import Fan
from service import Service
from install import Install
from version import Version
from me import Me
from fw import Fw
from ipmi import Ipmi
from host import Host, User, Passw


class SubCmdFactory:
    Cmds = ['me', 'fan', 'service', 'nic', 'cpld', 'mac', 'ipmi', 'install', 'version', 
        'host', 'user', 'passw', 'fw']

    def Factory(self, type):
        """  base on the command to return the class
        """
        return globals()[str(type.capitalize())]()

    @classmethod
    def getCmds(cls):
        """ Return all of the supported command so that it will can be used to register in shell
        """
        return cls.Cmds

