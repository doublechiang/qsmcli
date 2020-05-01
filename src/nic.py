#!/usr/bin/env python3

import os, sys
import logging
import subcmd
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg

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

    def __init__(self, arg=None):
        self.subs = {
            "dedicate": IpmiMsg(self.composeList(Nic.bmc_nic_set, 0)),
            "lom-share": IpmiMsg(self.composeList(Nic.bmc_nic_set, 1)),
            "mezz-share0": IpmiMsg(self.composeList(Nic.bmc_nic_set, 2)),
            "mezz-share1": IpmiMsg(self.composeList(Nic.bmc_nic_set, 3))
        }
        self.supported_cmds=  self._buildSupportCmds(self.subs)

