#!/usr/bin/env python3

import os, sys
import logging
import inspect
import subcmd
from ipmimsg import IpmiMsg
from ipmiexec import IpmiExec


class Fan(subcmd.SubCmd):
    """ fan commands: duty and auto to set fan duty and auto fan speed control.
    fan duty [index] [duty]
    :index fan index number [0-7]
    :duty 1-100
    fan auto
    description: set the fan in manual or in auto mode
    """
    AUTO_CMD = [ 0x30, 0x39, 1, 0xf0, 0xff, 0xff]
    DUTY_CMD = [ 0x30, 0x39, 0, 0]

    def duty(self, arg):
        """ Callback function for fan duty parameters
        geneate the index and the duty for "fan duty" command
        """
        logging.info('%s, arg=%s', inspect.currentframe().f_code.co_filename, arg)
        try:
            index, duty = self.__parse_arg(arg)
            cmd = self.composeList(Fan.DUTY_CMD, index, duty)
            IpmiExec().run(IpmiMsg(cmd))
        except ValueError:
            print(self.__doc__)

    def __parse_arg(self, arg):
        token=arg.split()
        if len(token) != 3:
            raise ValueError
        # check if fan index between 0-7
        val1 = int(token[1])
        if (val1 < 0) or (val1 > 7):
            raise ValueError
        val2 = int(token[2])
        if (val2 < 1 ) or (val2 > 100):
            raise ValueError
        return (val1, val2)


    def __init__(self, arg=None):

        self.subs = {
            "duty" : self.duty,
            "auto" : IpmiMsg(Fan.AUTO_CMD),
        }
        self.supported_cmds = self._buildSupportCmds(self.subs)
