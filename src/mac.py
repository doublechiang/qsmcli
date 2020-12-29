#!/usr/bin/env python3

import os, sys
import logging
import subcmd
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg


class Mac(subcmd.SubCmd):
    """
    get system mac command and print out the system mac we have
    mac [index], index range from 0 to 5
    for example: mac 0
    """

    GET_MAC_CMD = [0x30, 0x19]

    def mac(self, arg):
        try:
            index = self.__parse_arg(arg)
            msg = IpmiMsg(self.composeList(Mac.GET_MAC_CMD, index, 0))
            output = IpmiExec().run(msg).output()
            outlist = output.split()

            if outlist[0] == "05":
                self.__print_ieee(outlist[2:8])
        except ValueError:
            print(self.__doc__)
        except:
            logging.warning("Mac addresss not presented.")

    def __parse_arg(self, arg):
        """ Return the mac address string format
        """
        if len(arg.split()) != 1:
            logging.error("do not have mac index")
            raise ValueError
        if int(arg) < 0 or int(arg) > 5:
            logging.error("arguments out of index")
            raise ValueError
        return int(arg)

    def __print_ieee(self, arg):
        for token in arg[:-1]:
                print(token, end='')
                print(':', end='')
        print(arg[-1])

    def __init__(sefl):
        self.subs = self.mac


