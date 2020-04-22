#!/usr/bin/env python3

import os, sys
import logging
import subcmd
from globalvars import GlobalVars
from ipmiexec import IpmiExec

class Nic(subcmd.SubCmd):
    """
    get, set the BMC dedicate/share NIC
    nic [dedicate|lom-share|mezz-share0|mizz-share1]

    Return: <complete code> <LAN Card Type>
    For LAN Card Type,
    0h- BMC Dedicated
    2h- Shared NIC (OCP Mezzanine slot)
    3h- Shared NIC (QCT Mezzanine slot)
    """

    bmc_nic_set = [0x0c, 1, 1, 0xff]
    supported_cmds = [ 'dedicate', 'lom-share', 'mezz-share0', 'mizz-share1' ]

    def __validate_arg(self, arg):
        try:
            if arg is None or len(arg.split()) == 0:
                raise ValueError

            if len(arg.split()) > 0:
                if not arg.split()[0] in self.cmds:
                    raise ValueError
        except ValueError:
            self.not_supported()
            return False

        return True

    def __init__(self, arg=None):
        super().__init__(arg)
        self.cmds = {
            "dedicate": IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [0]),
            "lom-share": IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [1]),
            "mezz-share0": IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [2]),
            "mezz-sahre1": IpmiExec().marshal_raw_cmds(Nic.bmc_nic_set, [3])
        }
        self.__validate_arg(arg)

