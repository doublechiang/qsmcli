#!/usr/bin/env python3

import os, sys
import logging
from globalvars import GlobalVars
from sub_command import SubCommand
from ipmiexec import IpmiExec

class Fan(SubCommand):
    """ fan commands: duty and auto to set fan duty and auto fan speed control.
    fan duty [index] [duty]
    :index fan index number
    :duty 1-100
    fan auto
    description: set the fan in manual mode.
    """
    supported_cmds = ['auto', 'duty']

    AUTO_CMD = [ 0x30, 0x39, 1, 0xf0, 0xff, 0xff]
    DUTY_CMD = [ 0x30, 0x39, 0, 0]

    def setUp(self, ipmiexec):
        """ Callback function for fan duty parameters
        geneate the index and the duty for "fan duty" command
        """
        print(Fan.DUTY_CMD)
        logging.debug("composing FAN duty cmds=%s, %s, %s", Fan.DUTY_CMD, self.index, self.duty)
        ipmiexec.marshal_raw_cmds(Fan.DUTY_CMD, [self.index, self.duty])

    def __validate_arg(self, arg):
        try:
            token=arg.split()
            if len(token) != 3:
                raise ValueError
            # check if fan index between 0-7
            val1 = int(token[1])
            if (val1 < 0) or (val1 > 7):
                raise ValueEerror
            self.index = val1
            val2 = int(token[2])
            if (val2 < 1 ) or (val2 > 100):
                raise ValueError
            self.duty = val2
        except:
            self.not_supported()
            return False
        return True



    def __init__(self, arg=None):
        super().__init__(arg)

        self.cmds = {
            "duty" : IpmiExec(setup=self.setUp).marshal_raw_cmds(Fan.DUTY_CMD),
            "auto" : IpmiExec().marshal_raw_cmds(Fan.AUTO_CMD),
        }
        self.__validate_arg(arg)
