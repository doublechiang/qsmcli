#!/usr/bin/env python3

import os, sys
import logging
import inspect

# local moduels defined below
import ipmiexec
from interface import Interface
from ipmimsg import IpmiMsg
from abc import ABC
from abc import ABCMeta, abstractmethod


class SubCmd(ABC):
    """
        Definition of comamnds types
        There are 3 types commands action, they are IpmiMsg, Fucntion or a Dictionary indexed with following functions with function.

    """
    supported_cmds = []

    def not_supported(self):
        print(self.__doc__)

    def run(self, arg):
        """ run this commands, according subs variable.

            if the item value is a raw commands, then send out the command
            if the item value is a function, then call this function, it contain dynamic method.
            if the it contain a SubCommand, then it have more depth value.

        :param str arg: comamnds string arguments
        """
        logging.info('%s', inspect.currentframe().f_code.co_filename)
        action = self.getAction(arg)
        if (isinstance(action, IpmiMsg)):
            ipmiexec.IpmiExec().run(action)
        elif hasattr(action, '__call__'):
            action(arg)
        elif isinstance(action, str):
            print(action)


    def getAction(self, arg):
        """ return IpmiMsg/Function/SubCommand drived class based on parameters.
            depends on the instance attribute subs type
            if it's not a dictionary, then it's an action it self.
            If it's a action, then according to the argument to choose the required action.
        """
        if not isinstance(self.subs, dict):
            return self.subs
        else:
            params = arg.split()
            if (len(params) > 0 ):
                token = params[0]
                logging.info('token=%s, subs=%s', token, self.subs)
                if (isinstance(self.subs, dict)):
                    if token in self.subs:
                        return self.subs.get(token)  
        return self.__doc__

    @classmethod
    def composeList(cls, params, *argv):
        """ Compose everything into a list
        """
        if isinstance(params, list):
            result = params.copy()
        else:
            result = [params]
        for item in argv:
            if isinstance(item, list):
                result = result + item
            else:
                result.append(item)
        return result
            

    @classmethod
    @DeprecationWarning
    def _buildSupportCmds(cls, cmds):
        """ Helper function to build the class attribute from subcommands dicionary
        """
        cls.supported_cmds = []
        if isinstance(cmds, dict):
            cls.supported_cmds = cmds.keys()

    def getSupportCmds(self):
        """ return supported commands based on subs attribute.
        """
        cmds = []
        if isinstance(self.subs, dict):
            cmds = self.subs.keys()
        return cmds

    def __init__(self):
        self.subs = {}



