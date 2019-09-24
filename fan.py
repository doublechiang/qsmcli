#!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars
from sub_command import SubCommand
from ipmiexec import IpmiExec

class Fan(SubCommand):
    """ fan commands: duty and auto to set fan duty and auto fan speed control.
    fan duty [index] [duty]
    :index fan index number
    :duty 1-100
    fan auto
    description: set the fan in manual mode.
    """

    auto_cmd = [ 0x30, 0x39, 1, 0xf0, 0xff, 0xff]
    duty_cmd = [ 0x30, 0x39, 0, 0]

    @staticmethod
    def supported_cmds():
        return ['auto', 'duty']

    def auto(self, arg):
        """
        Fan auto commands do not require additional arguments.
        """
        exec = IpmiExec().marshal_raw_cmds(Fan.auto_cmd).run(printcmd=True)

    def set_duty(self, arg):
        try:
            if len(arg) != 2:
                raise ValueError

            # check if fan index between 0-7
            val = int(arg[0])
            if (val < 0) or (val > 7):
                raise ValueError
            val = int(arg[1])
            if (val < 1 ) or (val > 100):
                raise ValueError
        except:
            self.not_supported()
            return


        IpmiExec().marshal_raw_cmds(Fan.duty_cmd, [int(x) for x in arg]).run(printcmd=True)


    def __init__(self, arg):
        arglist = arg.split()
        if len(arglist) == 0:
            self.not_supported()
            return

        switcher = {
            "auto": self.auto,
            "duty": self.set_duty,
            }
        func =  switcher.get(arglist[0], self.not_supported)
        func(arglist[1:])
        return
