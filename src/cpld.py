    #!/usr/bin/env python3

import os, sys
import logging
import subcmd
from ipmimsg import IpmiMsg

class Cpld(subcmd.SubCmd):
    """
    get CPLD information:
    cpld [fw|cksum|id]
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    def __init__(self):
        self.subs = {
            'fw' : IpmiMsg( [0x30, 0x17, 3]),
            'cksum' : IpmiMsg([0x30, 0x17, 1]),
            'id' : IpmiMsg([0x30, 0x17, 2])
        }

