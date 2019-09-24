    #!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from ipmiexec import IpmiExec
from sub_command import SubCommand

class Cpld(SubCommand):
    """ CPLD sub commands:
    fw: get CPLD fw
    cksum: get CPLD checksum
    id: Get CPLD idcode
    """

    cpld_fw = [0x30, 0x17, 3]
    cpld_cksum = [0x30, 0x17, 1]
    cpld_id = [0x30, 0x17, 2]

    @staticmethod
    def supported_cmds():
        return ['fw', 'cksum', 'id']

    def invoke(self, cmdline):
        """ Calling CPLD raw command, and parsing the output
            Decoding is based on IPMI OEM spec.
        """
        exec = IpmiExec(cmdline).run(printcmd=True)
        return bytearray.fromhex(exec.output().rstrip())

    def fw(self):
        exec = IpmiExec().marshal_raw_cmds(Cpld.cpld_fw).run(printcmd=True)
        outbuf = exec.output()

    def cksum(self):
        exec = IpmiExec().marshal_raw_cmds(Cpld.cpld_cksum).run(printcmd=True)

    def id(self):
        exec = IpmiExec().marshal_raw_cmds(Cpld.cpld_id).run(printcmd=True)


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
