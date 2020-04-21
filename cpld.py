    #!/usr/bin/env python3

import os, sys
import logging
from globalvars import GlobalVars
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg
from sub_command import SubCommand

class Cpld(SubCommand):
    """
    get CPLD information:
    cpld [fw|cksum|id]
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    def __init__(self, arg=None):
        self.subs = { 
            'fw' : IpmiMsg( [0x30, 0x17, 3]),
            'cksum' : IpmiMsg([0x30, 0x17, 1]),
            'id' : IpmiMsg([0x30, 0x17, 2])
            }
        super().__init__(arg)

