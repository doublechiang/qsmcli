#!/usr/bin/env python3

import os, sys
import logging
from globalvars import GlobalVars
from ipmiexec import IpmiExec
from sub_command import SubCommand

class Me(SubCommand):
    """
    Query ME related information.
    me [version|cpu|dimm|io] 

    me version: to get ME version
    me cpu: to get CPU utililization
    me dimm: to get DIMM utililization
    me io: to get IO utilization
    """

    CPU_UTIL = [0x4, 0x2d, 0xbe]
    DIMM_UTIL = [0x4, 0x2d, 0xc0]
    IO_UTIL = [0x4, 0x2d, 0xbf]
    FW_VER = [6, 1]

    supported_cmds = ['version', 'cpu', 'dimm', 'io']

    def __validate_arg(self, arg):
        try:
            if arg is None or len(arg.split()) == 0:
                raise ValueError

            if len(arg.split()) > 0:
                if not arg.split()[0] in self.cmds:
                    raise ValueError
        except ValueError:
            self.not_supported()
            return False

        return True



    def __init__(self, arg=None):
        super().__init__(arg)
        self.cmds = {
            "version" : IpmiExec(bridge=0x2c, channel=6).marshal_raw_cmds(Me.FW_VER),
            "cpu" : IpmiExec(bridge=0x2c, channel=6).marshal_raw_cmds(Me.CPU_UTIL),
            "dimm" : IpmiExec(bridge=0x2c, channel=6).marshal_raw_cmds(Me.DIMM_UTIL),
            "io" : IpmiExec(bridge=0x2c, channel=6).marshal_raw_cmds(Me.IO_UTIL)
        }
        self.__validate_arg(arg)
