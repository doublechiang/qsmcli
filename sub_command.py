#!/usr/bin/env python3

import os, sys
import logging
from globalvars import GlobalVars
from ipmiexec import IpmiExec

class SubCommand():

    """ SubCommands interface.
        If there is no other sub commands,
    """
    supported_cmds = []

    def not_supported(self):
        print(self.__doc__)

    def run(self):
        # if command it has ipmiexec defined, then we should call it.
        try:
            logging.debug("self.cmds=%s", self.cmds)
            if isinstance(self.cmds, IpmiExec):
                logging.debug("calling %s", self.cmds)
                self.cmds.run()
                return

            # if CMDS defined, then we should call dispatched ipmiexec objects
            if isinstance(self.cmds, dict):
                logging.debug("self.cmds = %s", self.cmds)
                if len(list(self.cmds.keys())) > 0:
                    # we can improve here, sometimes the commands without further parameter still a valid command.
                    if len(self.arg.split()) > 0:
                        token = self.arg.split()[0]
                        obj = self.cmds.get(token, self.not_supported)
                        if isinstance(obj, IpmiExec):
                            logging.debug("value in dictionary is %s", obj)
                            obj.run(printcmd=True)
                            return
        except AttributeError:
            logging.error("Attribute has error, self.cmds=%s", self.cmds)

    def __init__(self, arg=None):
        logging.debug("%s, arg is %s, type is %s", self.__init__, arg, type(arg))
        self.arg =  arg
