    #!/usr/bin/env python3

import os, sys
from globalvars import GlobalVars

class SubCommand():

    """ SubCommands interface.
        If there is no other sub commands,
    """

    def supported_cmds(self):
        return list(self.CMDS.keys())

    def not_supported(self):
        print(self.__doc__)

    def do_self(self):
        print("implement this function when there is no following arguemtns")

    def __init__(self, arg=None):
        if arg is None:
            return
            
        # if no CMDS defined
        if len(list(self.CMDS.keys())) == 0:
            # if no argument, should call do_self, else, show document
            if len(arg.split()) == 0:
                self.do_self()
            else:
                self.not_supported()
        else:  # if CMDS defined. check if arguement is matched, othewise show document
            if len(arg.split()) == 0:
                self.not_supported()
            else:
                token = arg.split()[0]
                obj = self.CMDS.get(token, self.not_supported)
                if callable(obj):
                    obj()
