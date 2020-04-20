#!/usr/bin/env python3

import os, sys
import logging
import inspect
import ipmiexec
from globalvars import GlobalVars
from abc import ABC
from abc import ABCMeta, abstractmethod


class SubCommand(ABC):
    """ SubCommands abstract class.
        A class, input is the command argument
        should send out the leverage the command to next lower layer, and process the output
    """
    supported_cmds = []
    subs = {}

    def not_supported(self):
        print(self.__doc__)

    def run(self):
        """ run this commands, according subs dictionary.
            if the item value is a raw commands, then send out the command
            if the item value is a function, then call this function, it contain dynamic method.
            if the it contain a SubCommand, then it have more depth value.
        """
        logging.info('%s, base subcommands run', inspect.currentframe().f_code.co_filename)
        token = self.arg.split()[0]             # argument is safe, get the argument
        logging.info('subs definition %s', self.subs)
        value = self.subs.get(token)                 # get the target objects.
        logging.info('token=%s, value=%s', token, value)
        if (isinstance(value, IpmiMsg)):
            logging.info("it's IpmiMsg, token=%s", token)
            ipmiexec.IpmiExec().run(value)


    @abstractmethod
    def _validate_arg():
        pass

    
    def __init__(self, arg=None):
        self.arg = arg

class IpmiMsg():
    """ Ipmi message object.
    """
    def format(self):
        """ return the parameters for ipmitool 
        """
        str = ""
        if self.brdg:
            str = str + "-t {bridge} ".format(bridge=self.brdg)
        if self.chnl:
            str = str + "-b {channel} ".format(channel=self.chnl)

        raw_str = "raw "
        for raw_byte in self.raw:
            raw_str += "0x%x " % raw_byte

        str = str + raw_str
        return str

    def __init__(self, raw=[], brdg=None, chnl=None):
        self.raw = raw
        self.brdg = brdg
        self.chnl = chnl

