#!/usr/bin/env python3

import os
import sys
import logging

# third pary librarys
from elevate import elevate

# local modules
import subcmd

class Install(subcmd.SubCmd):

    """ Install this application into OS's path library
        In Linux, create the symbloic link in the /usr/local/bin
        In Windows, append application folder into system path variable.
    """

    WINBAT='qsmcli.bat'

    def install(self, arg=None):
        if ('posix' == os.name):
            self.install_in_linux(arg)
        else:
            self.install_in_win(arg)


    def install_in_linux(self, arg):
        """ Create the symbolic name in /usr/local/bin directory
        """
        LOCAL_BIN='/usr/local/bin/'
#        elevate(graphical=False)
        elevate()
        basename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        print(basename)
        src = os.path.abspath(sys.argv[0])
        dest = LOCAL_BIN+basename
        if os.path.isfile(dest):
            logging.warning("Destination file %s exist, overwriting it.", dest)
            os.unlink(dest)
        logging.critical("Creating symbolic link %s to %s ", dest, src)
        os.symlink(src, dest)

    def install_in_win(self, arg):
        """ create a bat file in the window32 folder and start this application
        """

        # We would like to put the file in system32 folderself.
        # However, the windows will redirect the system32 directory call
        # so use the sysnative folder actuall point to system32 folder
        sys32dir = os.environ['WINDIR'] + '\\sysnative\\'
        winbat_file = sys32dir + Install.WINBAT

        try:
            # Check if file pre-exist and file permission
            if os.path.isfile(winbat_file):
                print("Destination file %s exist, overwriting it." % winbat_file)
                os.unlink(winbat_file)
                if os.path.isfile(winbat_file):
                    print("Error! file can't be deleted")
                    return

            # Create the batch file
            pgm = os.path.abspath(sys.argv[0])
            with open(winbat_file, 'w') as bat_file:
                print("creating %s" % winbat_file)
                bat_file.write("start \"\" \"%s\" %*" % pgm)

        except IOError:
            print("Write file error, run program as administrator")
            return
        except:
            print("Please return error to author for your money back")

    def __init__(self):
        self.subs =  self.install
