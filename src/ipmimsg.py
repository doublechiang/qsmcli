#!/usr/bin/env python3

import os, sys
import logging

class IpmiMsg():
    """ Ipmi message object.
    """
    def format(self):
        """ return the parameters for ipmitool 
        """
        str = ""
        if self.brdg:
            str = str + "-t 0x{bridge:x} ".format(bridge=self.brdg)
        if self.chnl:
            str = str + "-b 0x{channel:x} ".format(channel=self.chnl)

        raw_str = "raw "
        for raw_byte in self.raw:
            raw_str += "0x%x " % raw_byte

        str = str + raw_str
        return str

    def __init__(self, raw=[], brdg=None, chnl=None):
        self.raw = raw
        self.brdg = brdg
        self.chnl = chnl


    def __eq__(self, other):
        if self.raw == other.raw and self.brdg == other.brdg and self.chnl == other.chnl:
            return True
        return False


