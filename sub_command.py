#!/usr/bin/env python3

import os, sys
import logging
import inspect
import ipmiexec
from globalvars import GlobalVars
from abc import ABC
from abc import ABCMeta, abstractmethod


class SubCommand(ABC):
    """
        Definition of subs.
        There are 3 types commands action, they are IpmiMsg, Fucntion or a Dictionary

    """

    def not_supported(self):
        print(self.__doc__)

    def run(self, arg):
        """ run this commands, according subs dictionary.
            if the item value is a raw commands, then send out the command
            if the item value is a function, then call this function, it contain dynamic method.
            if the it contain a SubCommand, then it have more depth value.
        """
        logging.info('%s', inspect.currentframe().f_code.co_filename)
        action = self.getAction(arg)
        if (isinstance(action, IpmiMsg)):
            ipmiexec.IpmiExec().run(action)
        elif isinstance(action, str):
            print(action)

    def getAction(self, arg):
        """ According to the parameter, return the action.
        """
        params = arg.split()
        if (len(params) > 0 ):
            token = params[0]
            logging.info('token=%s, subs=%s', token, self.subs)
            if (isinstance(self.subs, dict)):
                if token in self.subs:
                    return self.subs.get(token)  
        return self.__doc__


    
    def __init__(self, arg=None):
        # If the subs contain a list, then it's the support commands for reference
        logging.info('init..., self.subs =%s', self.subs)
        if isinstance(self.subs, dict):
            self.supported_cmds = self.subs.keys()


