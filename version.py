#!/usr/bin/env python3

import os
import sys

class Version():
    """
    Show version and credit information.
    Bug repoort and Suggestion please visit https://github.com/doublechiang/qsmcli
    """
    VERSION='0.4'

    def __init__(self):
        pass

    def __str__(self):
        return Version.VERSION


if __name__ ==  "__main__":
    print(Version().__str__())
