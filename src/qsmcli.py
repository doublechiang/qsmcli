#!/usr/bin/env python3
import sys
import os
import subprocess
import argparse
import logging



# local modules
from subcmdfactory import SubCmdFactory
from qsmshell import QsmShell
from version import Version
from config import Config


class Qsmcli():
    """ Command line mode do not preserver any settings, this will cause un-consistence.
    shell mode will try to keep the previous data as much as possible.
    """

    def run(self):
        self.process_argument()

    def process_argument(self):

        # Add optional arguments
        parser = argparse.ArgumentParser()
        # TODO, read a file contain IP list then process it.
        # parser.add_argument("-f", "--filename", dest="filename",
        #    help="Read IP addresses from the filename")
        parser.add_argument("-U", "--username", dest="username",
            help="Assing username for IPMI session")
        parser.add_argument("-P", "--password", dest="password",
            help="Assing password for IPMI session")
        parser.add_argument("-H", "--host", dest="host",
            help="Assing Host for IPMI session")
        parser.add_argument('--version', action='version', version= '%(prog)s ' + Version().__str__()  )

        # add the positional argument, they are first level 
        parser.add_argument("cmd", nargs="*", help="major subcommand")
        args = parser.parse_args(sys.argv)
        
        # Processing optional Argument, if the option arguement exist, then processs it all
        
        options = dict()
        if args.username:
            options['username'] = args.username
        if args.password:
            options['password'] = args.password
        if args.host:
            options['host'] = args.username

        # If there are any positional argument, launch the command mode
        logging.info(args.cmd)
        if (len(args.cmd)>1):
            if args.cmd[1] in Qsmcli.Cmds:
                pass
        else:
            shell = QsmShell(persistent_history_file= Config.getHistoryFnPath())
            
            shell.regCmds(SubCmdFactory.getCmds())
            shell.cmdloop()


if __name__ == "__main__":
#    logging level [DEBUG|INFO|WARNING]
    logging.basicConfig(level=logging.WARNING)
#    logging.basicConfig(level=logging.INFO)
    # print(globals()['Fw']())
    Qsmcli().run()
