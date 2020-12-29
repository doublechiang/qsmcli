#!/usr/bin/env python3

import os
import sys
import subcmd 

class Version(subcmd.SubCmd):
    """
    Show version and credit information.
    Bug repoort and Suggestion please visit https://github.com/doublechiang/qsmcli
    """
    VERSION='0.7.1'

    def printVersion(self, arg):
        print(self)

    def __str__(self):
        return Version.VERSION

    def __init__(self):
        self.subs = self.printVersion


if __name__ ==  "__main__":
    print(Version())
