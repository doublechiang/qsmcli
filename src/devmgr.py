#!/usr/bin/env python3

from ipmiexec import IpmiExec
from ipmimsg import IpmiMsg


class DevMgr:
    DEVID_S2B = 0x3242
    DEVID_S2P = 0x3250
    DEVID_S2S = 0x3253

    DEVID_S5B = 0x3542
    DEVID_S5BQ = 0x3542
    DEVID_S5BE = 0x3542
    DEVID_S5D = 0x3544
    DEVID_S5T = 0x3554


    GRP_PURLEY = [DEVID_S5B, DEVID_S5D, DEVID_S5T]
    GRP_GRANTLEY = [DEVID_S2B, DEVID_S2P, DEVID_S2S]

    GRPID_PURLEY = 'S5x'
    GRPID_GRANTLEY = 'S2x'
    GRPID_UNKNOWN = 'Unknown'

    def getId(self):
        output = self.__mc_info()
        for line in output.splitlines():
            if line.startswith('Product ID'):
                value = line.split(':')[1]
                return int(value.split()[0])

    def getGrp(self):
        """ Get Group Identification, return 'S5x', 'S2x', 'Unknown'
        """
        id = self.getId()
        if id in DevMgr.GRP_PURLEY:
            return DevMgr.GRPID_PURLEY
        elif id in DevMgr.GRP_GRANTLEY:
            return DevMgr.GRPID_GRANTLEY
        else:
            return DevMgr.GRPID_UNKNOWN


    def __mc_info(self):
        msg  = IpmiMsg("mc info")
        output = IpmiExec().run(msg, printcmd=False).output()
        return output


