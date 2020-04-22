#!/usr/bin/env python3

import os, sys
import logging
import subcmd
from globalvars import GlobalVars
from ipmiexec import IpmiExec


class Mac(subcmd.SubCmd):
    """
    get system mac command and print out the system mac we have
    mac [index], index range from 0 to 5
    for example: mac 0
    """

    GET_MAC_CMD = [0x30, 0x19]

    def setUp(self, ipmiexec):
        ipmiexec.marshal_raw_cmds(ipmiexec.raw, [int(self.arg.split()[0]), 0])

    def parser(self, arg):
        """ Return the mac address string format
        """
        logging.debug("called in %s, arg is %s", self.parser, arg)
        arglist = arg.split()
        if len(arglist) == 0:
            return

        if arglist[0] == "05":
            self.__print_ieee(arglist[2:8])
        else:
            logging.warning("Mac addresss not presented.")

    def __print_ieee(self, arg):
        for token in arg[:-1]:
                print(token, end='')
                print(':', end='')
        print(arg[-1])

    def __validate_arg(self, arg):
        if arg is None:
            return False

        try:
            if len(arg.split()) != 1:
                logging.error("do not have mac index")
                raise ValueError
            if int(arg) < 0 or int(arg) > 5:
                logging.error("arguments out of index")
                raise ValueError

        except ValueError:
            self.not_supported()
            return False
        return True


    def __init__(self, arg=None):
        super().__init__(arg)
        self.cmds=None  
        if self.__validate_arg(arg):
            self.cmds=IpmiExec(raw=Mac.GET_MAC_CMD, setup=self.setUp, parser=self.parser)
