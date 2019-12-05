#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
import install
import logging
from qsmshell import QsmShell
from globalvars import GlobalVars
from mac import Mac
from cpld import Cpld
from nic import Nic
from fan import Fan
from service import Service
from me import Me

from install import Install
from version import Version


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
        parser.add_argument('--version', action='version', version= '%(prog)s ' + Version().__str__()  )

        subp = parser.add_subparsers()
        parser_fan= subp.add_parser('fan')
        parser_fan.add_argument('fan_sub', nargs="*", choices=Fan.supported_cmds)
        parser_service= subp.add_parser('serivce')
        parser_service.add_argument('service_sub', nargs="*", choices=Service.supported_cmds)
        parser_sdr= subp.add_parser('mac')
        #mac has single command with index followed, no supported commands follwed.
        # parser_sdr.add_argument('mac_sub', nargs="*", choices=Mac().supported_cmds())
        parser_sdr= subp.add_parser('nic')
        parser_sdr.add_argument('nic_sub', nargs="*", choices=Nic.supported_cmds)
        parser_sdr= subp.add_parser('cpld')
        parser_sdr.add_argument('cpld_sub', nargs="*", choices=Cpld.supported_cmds)
        parser_sdr= subp.add_parser('me')
        parser_sdr.add_argument('me_sub', nargs="*", choices=Me.supported_cmds)
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
            'mac_sub': (lambda self, x: QsmShell.do_mac(self, x)),
            'nic_sub': (lambda self, x: QsmShell.do_nic(self, x)),
            'cpld_sub': (lambda self, x: QsmShell.do_cpld(self, x)),
            'me_sub': (lambda self, x: QsmShell.do_me(self, x)),
            'fan_sub': (lambda self, x: QsmShell.do_fan(self, x)),
            'service_sub': (lambda self, x: QsmShell.do_service(self, x)),
            'ipmi_sub': (lambda self, x: QsmShell.do_ipmi(self, x)),
            'install': (lambda self,x:QsmShell.do_install(self.x)),
            'version': (lambda self,x:QsmShell.do_version(self.x)),
        }
        cmd_mode=None
        for key, func in sub_commands.items():
            if (hasattr(self.args, key)):
                shell = QsmShell()
                sub_commands[key](shell, ' '.join(getattr(self.args, key)))
                cmd_mode=True
                break

        if cmd_mode is not True:
            shell = QsmShell(persistent_history_file= GlobalVars.get_history_file_path())
            shell.setPrompt()
            shell.cmdloop()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
#    logging.basicConfig(level=logging.WARNING)
    qsmcli= Qsmcli(sys.argv)
    GlobalVars.load()
    qsmcli.process_argument()
    GlobalVars.save()
