#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
from qsmshell import QsmShell
from globalvars import GlobalVars
from sdr import Sdr

__version__="0.2"


def main():


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
    parser_ipmi = subp.add_parser('ipmi')
    parser_ipmi.add_argument('ipmi_sub', nargs="*")

    args = parser.parse_args()
    print (args)

    # Processing optional Argument
    if args.filename:
        with open(args.filename) as f:
            ip_lists = [x.strip() for x in f.readlines()]
    if args.username:
        GlobalVars.username = args.username
    if args.password:
        GlobalVars.password = args.password
    # Processing argument, if any of the argements is presented, enter the command mode.
    # There is only one argement is allowed.
#    if args.sdr:
#        print("arg sdr is called"+ args.sdr)
#    if args.ipmi:
#        print("arg ipmi is specified")

    GlobalVars.load()
    shell = QsmShell()
    shell.setPrompt()
    shell.cmdloop()
    GlobalVars.save()


if __name__ == "__main__":
    """ Command line mode do not preserver any settings, this will cause un-consistence.
        shell mode will try to keep the previous data as much as possible.
        """
    main()
