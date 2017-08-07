#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
from qsmshell import QsmShell
from globalvars import GlobalVars

__version__="0.1"


def main():


    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", dest="filename",
                      help="Read IP addresses from the filename")
    parser.add_argument("-U", "--username", dest="username",
                      help="Assing username for IPMI session")
    parser.add_argument("-P", "--password", dest="password",
                      help="Assing password for IPMI session")
    parser.add_argument('--version', action='version', version= '%(prog)s ' + __version__  )
    args = parser.parse_args()

    if args.filename:
        with open(args.filename) as f:
            ip_lists = [x.strip() for x in f.readlines()]

    if args.username:
        GlobalVars.username = args.username

    if args.password:
        GlobalVars.password = args.password

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
