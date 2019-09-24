    #!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars

class SubCommand():

    """ SubCommands interface.
    """

    @staticmethod
    def supported_cmds():
        pass

    def not_supported(self):
        print(self.__doc__)
