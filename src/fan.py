#!/usr/bin/env python3

import os, sys
import logging
import inspect
import subcmd
from ipmimsg import IpmiMsg
from ipmiexec import IpmiExec

from devmgr import DevMgr


class Fan(subcmd.SubCmd):
    """ fan commands: duty and auto to set fan duty and auto fan speed control.
    fan duty [index] [duty]
    :index fan index number [0-7]
    :duty 1-100
    fan auto
    description: set the fan in manual or in auto mode

    platform: Purley & S2B/S2S has different format
    For S2B/S2Sx,  0x30 0x39 [mode] [source] [number] [duty]
        mode: 1: manual, 2: auto
        source: 0:PWM, 1: W83793, 2:NCT7802Y (PCIE FAN)
        number: Fan number
        duty: 00-64h: PWM, 00-3fh: W83793, 00-ffh:NCT7802Y (PCIE FAN)
    """
    AUTO_CMD = [ 0x30, 0x39, 1, 0xf0, 0xff, 0xff]
    DUTY_CMD = [ 0x30, 0x39, 0, 0]
    S2B_DUTY_CMD = [ 0x30, 0x39, 1, 0 ]
    S2B_AUTO_CMD = [0x30, 0x39, 2, 0, 0, 0]

    def duty(self, arg):
        """ Callback function for fan duty parameters
        geneate the index and the duty for "fan duty" command
        """
        logging.info('%s, arg=%s', inspect.currentframe().f_code.co_filename, arg)
        try:
            index, duty = self.__parse_arg(arg)
        except ValueError:
            print(self.__doc__)

        devid = DevMgr().getId()
        if devid == DevMgr.DEVID_S2B or devid == DevMgr.DEVID_S2S:
            cmd = self.composeList(Fan.S2B_DUTY_CMD, index, duty)
        else:
            cmd = self.composeList(Fan.DUTY_CMD, index, duty)
        IpmiExec().run(IpmiMsg(cmd))

    def auto(self, arg):
        devid = DevMgr().getId()
        if devid == DevMgr.DEVID_S2B or devid == DevMgr.DEVID_S2S:
            msg = IpmiMsg(Fan.S2B_AUTO_CMD)
        else:
            msg = IpmiMsg(Fan.AUTO_CMD)
        IpmiExec().run(msg)

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

    def __init__(self):
        self.subs = {
            "duty" : self.duty,
            "auto" : self.auto
        }
