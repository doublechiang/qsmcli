    #!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from exec import Exec

class Cpld():
    """ CPLD sub commands:
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    @staticmethod
    def supported_cmds():
        return ['fw', 'cksum', 'id']

    def invoke(self, cmdline):
        """ Calling CPLD raw command, and parsing the output
            Decoding is based on IPMI OEM spec.
        """
        exec = Exec(cmdline, printcmd=True)
        return bytearray.fromhex(exec.output().rstrip())

    def fw(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x03"
        out = self.invoke(cmdline)
        print("Completion Code: ", format(out[0], '02x'))
        print("CPLD Version: ", out[1:5])

    def cksum(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x01"
        out = self.invoke(cmdline)
        print("Completion Code: ", format(out[0], '02x'))
        print("Checksum: ", out[1:3])

    def id(self):
        cmdline = GlobalVars.host_access() + " raw 0x30 0x17 0x02"
        out = self.invoke(cmdline)
        print("Completion Code: ", format(out[0], '02x'))
        print("ID Code: ", out[1:5])


    def not_supported(self):
        print("Not supported commands")
        print(Cpld.__doc__)


    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (Cpld.__doc__)
            return

        switcher = {
            "fw": self.fw,
            "cksum": self.cksum,
            "id": self.id,
            }
        func =  switcher.get(arg, self.not_supported)
        func()
