#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from ipmiexec import IpmiExec

class Nic():
    """ nic command: get, set the NIC dedicate/share NIC
    nic dedicate
    nic lom-share
    nic mezz-share0
    nic mizz-share1
    nic: print the supported sub commands.

    Return: <complete code> <LAN Card Type>
    For LAN Card Type,
    0h- BMC Dedicated
    2h- Shared NIC (OCP Mezzanine slot)
    3h- Shared NIC (QCT Mezzanine slot)
    """

    bmc_nic_set = [0x0c, 1, 1, 0xff]

    @staticmethod
    def supported_cmds():
        return ['dedicate', 'lom-share', 'mezz-share0', 'mezz-share1']

    def dedicate(self):
        IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [0]).run(printcmd=True)

    def lom_share(self):
        IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [1]).run(printcmd=True)

    def mezz_share0(self):
        IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [2]).run(printcmd=True)

    def mezz_share1(self):
        IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [3]).run(printcmd=True)

    def __init__(self, arg):
        if len(arg.split()) == 0:
            print (self.__doc__)
            return

        switcher = {
            "dedicate": self.dedicate,
            "lom-share": self.lom_share,
            "mezz-share0": self.mezz_share0,
            "mezz-sahre1": self.mezz_share1,
            }
        func =  switcher.get(arg, print(self.__doc__))
        func()
        return None
