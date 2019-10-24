#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from ipmiexec import IpmiExec
from sub_command import SubCommand

class Me(SubCommand):
    """ Query ME related information.
    me version: to get ME version
    me cpu: to get CPU utililization
    me dimm: to get DIMM utililization
    me io: to get IO utilization
    """

    CPU_UTIL = [0x4, 0x2d, 0xbe]
    DIMM_UTIL = [0x4, 0x2d, 0xc0]
    IO_UTIL = [0x4, 0x2d, 0xbf]
    FW_VER = [6, 1]

    def parse_raw_response(self, arg):
        """ Return the mac address string format
        """
        print(arg)


    def getVersion(self):
        exec = IpmiExec().marshal_raw_cmds(Me.FW_VER).with_bridge(0x2c).with_channel(6).run(printcmd=True)
        self.parse_raw_response(exec.stdout.split())

    def getCpuUtil(self):
        exec = IpmiExec().marshal_raw_cmds(Me.CPU_UTIL).with_bridge(0x2c).with_channel(6).run(printcmd=True)
        self.parse_raw_response(exec.stdout.split())

    def getDimmUtil(self):
        exec = IpmiExec().marshal_raw_cmds(Me.DIMM_UTIL).with_bridge(0x2c).with_channel(6).run(printcmd=True)
        self.parse_raw_response(exec.stdout.split())

    def getIoUtil(self):
        exec = IpmiExec().marshal_raw_cmds(Me.IO_UTIL).with_bridge(0x2c).with_channel(6).run(printcmd=True)
        self.parse_raw_response(exec.stdout.split())


    def __init__(self, arg=None):
        self.CMDS = {
            "version" : self.getVersion,
            "cpu" : self. getCpuUtil,
            "dimm" : self.getDimmUtil,
            "io" : self.getIoUtil
        }

        super().__init__(arg)
        return
