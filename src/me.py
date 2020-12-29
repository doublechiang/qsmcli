#!/usr/bin/env python3

import os, sys
import logging
import inspect
import subcmd
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg

class Me(subcmd.SubCmd):
    """
    Query ME related information.
    me [version|cpu|dimm|io] 

    me version: to get ME version
    me cpu: to get CPU utililization
    me dimm: to get DIMM utililization
    me io: to get IO utilization
    """

    def __init__(self, arg=None):
        self.subs = { 
            'version' : IpmiMsg([6, 1], brdg=0x2c, chnl=6),
            'cpu' : IpmiMsg([0x4, 0x2d, 0xbe], brdg=0x2c, chnl=6),
            'dimm' : IpmiMsg([0x4, 0x2d, 0xc0], brdg=0x2c, chnl=6),
            'io': IpmiMsg( [0x4, 0x2d, 0xbf], brdg=0x2c, chnl=6)
            }

