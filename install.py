#!/usr/bin/env python3

import os
import sys
from globalvars import GlobalVars
from exec import Exec

class Install():
    """ Install this application into OS's path library
        In Linux, create the symbloic link in the /usr/local/bin
        In Windows, append application folder into system path variable.
    """

    def install_in_linux(self, arg):
        """ Create the symbolic name in /usr/local/bin directory
        """
        LOCAL_BIN='/usr/local/bin/'
        basename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        src = os.path.abspath(sys.argv[0])
        dest = LOCAL_BIN+basename
        if os.path.isfile(dest):
            print(f"Destination file {dest} exist, overwriting it.")
            os.unlink(dest)
        print(f"Creating symbolic link {dest} to {src}")
        os.symlink(src, dest)

    def install_in_win(self):
        print("Windows Installation not implement yet.")


    def __init__(self, arg):
        if ('posix' == os.name):
            self.install_in_linux(arg)
        else:
            self.install_in_win(arg)
