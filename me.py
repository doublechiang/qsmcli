#!/usr/bin/env python3

import os, sys
import logging
import inspect
from ipmiexec import IpmiExec
from sub_command import SubCommand
from sub_command import IpmiMsg

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

    def _validate_arg(self):
        """ Validate the arguments
            me command must have sub command for example version/cpu/dimm/io
        """
        logging.info('%s, validating argument, argument=%s', inspect.currentframe().f_code.co_filename, self.arg)
        try:
            if self.arg is None or len(self.arg.split()) == 0:
                raise ValueError

            if len(self.arg.split()) > 0:
                if not self.arg.split()[0] in Me.supported_cmds:
                    raise ValueError
        except ValueError:
            logging.error('%s, validating argument error', self.arg)
            self.not_supported()
            return False

        logging.info('Validated parameter succesful.')

        return True

    def __init__(self, arg=None):
        self.arg = arg
        self.subs = { 
            'version' : IpmiMsg(Me.FW_VER, brdg=0x2c, chnl=6),
            'cpu' : IpmiMsg(Me.CPU_UTIL, brdg=0x2c, chnl=6),
            'dimm' : IpmiMsg(Me.DIMM_UTIL, brdg=0x2c, chnl=6),
            'io': IpmiMsg(Me.IO_UTIL, brdg=0x2c, chnl=6)
            }

