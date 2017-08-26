#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
from qsmshell import QsmShell
from globalvars import GlobalVars
from sdr import Sdr
from sel import Sel
from mac import Mac
from cpld import Cpld
from nic import Nic

__version__="0.3"

class Qsmcli():
    """ Command line mode do not preserver any settings, this will cause un-consistence.
    shell mode will try to keep the previous data as much as possible.
    """
    def __init__(self, args):

        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--filename", dest="filename",
        help="Read IP addresses from the filename")
        parser.add_argument("-U", "--username", dest="username",
        help="Assing username for IPMI session")
        parser.add_argument("-P", "--password", dest="password",
        help="Assing password for IPMI session")
        parser.add_argument('--version', action='version', version= '%(prog)s ' + __version__  )

        subp = parser.add_subparsers()
        parser_sdr= subp.add_parser('sdr')
        parser_sdr.add_argument('sdr_sub', nargs="*", choices=Sdr.supported_cmds())
        parser_sdr= subp.add_parser('sel')
        parser_sdr.add_argument('sel_sub', nargs="*", choices=Sel.supported_cmds())
        parser_sdr= subp.add_parser('mac')
        parser_sdr.add_argument('mac_sub', nargs="*", choices=Mac.supported_cmds())
        parser_sdr= subp.add_parser('nic')
        parser_sdr.add_argument('nic_sub', nargs="*", choices=Nic.supported_cmds())
        parser_sdr= subp.add_parser('cpld')
        parser_sdr.add_argument('cpld_sub', nargs="*", choices=Cpld.supported_cmds())
        parser_ipmi = subp.add_parser('ipmi')
        parser_ipmi.add_argument('ipmi_sub', nargs="*")
        self.args = parser.parse_args(args[1:])

    def process_argument(self):
    # Processing optional Argument, if the option arguement exist, then processs it all
        if self.args.filename:
            with open(self.args.filename) as f:
                ip_lists = [x.strip() for x in f.readlines()]
        if self.args.username:
            GlobalVars.username = self.args.username
        if self.args.password:
            GlobalVars.password = self.args.password

    # Processing argument, if any of the argements is presented, enter the command mode.
    # There is only one argement is allowed.
        sub_commands= {
            'sdr_sub': (lambda self, x: QsmShell.do_sdr(self, x)),
            'sel_sub': (lambda self, x: QsmShell.do_sel(self, x)),
            'mac_sub': (lambda self, x: QsmShell.do_mac(self, x)),
            'nic_sub': (lambda self, x: QsmShell.do_nic(self, x)),
            'cpld_sub': (lambda self, x: QsmShell.do_cpld(self, x)),
            'ipmi_sub': (lambda self, x: QsmShell.do_ipmi(self, x)),
        }
        cmd_mode=None
        for key, func in sub_commands.items():
            if (hasattr(self.args, key)):
                shell = QsmShell()
                sub_commands[key](shell, ' '.join(getattr(self.args, key)))
                cmd_mode=True
                break

        if cmd_mode is not True:
            shell = QsmShell()
            shell.setPrompt()
            shell.cmdloop()


if __name__ == "__main__":
    qsmcli= Qsmcli(sys.argv)
    GlobalVars.load()
    qsmcli.process_argument()
    GlobalVars.save()
