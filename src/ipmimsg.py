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

        if isinstance(self.params, list):
            raw_str = "raw "
            for raw_byte in self.params:
                raw_str += "0x%x " % raw_byte
            str = str + raw_str
            return str
        else:
            # else it should be ipmitool string format
            return self.params

    def __init__(self, params, brdg=None, chnl=None):
        if not (isinstance(params, list) or isinstance(params, str)):
            raise AssertionError
        self.params = params
        self.brdg = brdg
        self.chnl = chnl


    def __eq__(self, other):
        if self.params == other.params and self.brdg == other.brdg and self.chnl == other.chnl:
            return True
        return False


