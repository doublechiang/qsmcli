#!/usr/bin/env python3

import os, sys
import logging

import subcmd
from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg

class Nic(subcmd.SubCmd):
    """
    get, set the BMC dedicate/share NIC
    nic [show|dedicate|lom-share|mezz-share0|mizz-share1]

    Return: <complete code> <LAN Card Type>
    For LAN Card Type,
    0h- BMC Dedicated
    2h- Shared NIC (OCP Mezzanine slot)
    3h- Shared NIC (QCT Mezzanine slot)
    """

    bmc_nic_set = [0x0c, 1, 1, 0xff]
    bmc_nic_get = [0xc, 2, 1, 0xff, 0, 0]
    DECODE_ERROR = "Cant' decode output result"


    def getNicMode(self, args):
        msg = IpmiMsg(cls.composeList(Nic.bmc_nic_get))
        outlist = IpmiExec().run(msg).output().split()
        if outlist[0] == '11':
            # bit [0:3] for NIC mode. 0 dedicated, 1, share- 2,3 share OCP mezzanine slot 
            mode = {
                '00': 'Dedicated NIC',
                '01': 'Share NIC',
                '02': 'Share NIC, OCP Mezzanine slot',
                '03': 'Share NIC, OCP Mezzanine slot'
            }
            print(mode.get(outlist[1], Nic.DECODE_ERROR))
        else:
            print(Nic.DECODE_ERROR)

    def __init__(self):
        self.subs = {
            "show": self.getNicMode,
            "dedicate": IpmiMsg(self.composeList(Nic.bmc_nic_set, 0)),
            "lom-share": IpmiMsg(self.composeList(Nic.bmc_nic_set, 1)),
            "mezz-share0": IpmiMsg(self.composeList(Nic.bmc_nic_set, 2)),
            "mezz-share1": IpmiMsg(self.composeList(Nic.bmc_nic_set, 3))
        }
