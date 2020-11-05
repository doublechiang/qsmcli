#!/usr/bin/env python3

import os, sys
import logging


import subcmd
from config import Config


class Host(subcmd.SubCmd):
    """ host command
        shell mode is implied to work on specific host, this is indicate on the prompt.
        host [ip] [user] [password]
        you can change the ip, if you supply more field, it will be treated as username & password.
    """

    def host(self, arg):
        try:
            count = len(arg.split())
            if count == 0:
                raise ValueError
            if count > 0:
                host = arg.split()[0]
                current = Config().current
                hosts = Config().hosts
                current['host'] = host

                if count == 1:
                    # if only host is provided, then check if host has been saved before
                    # if exist, then use the previous user & passw
                    cred = hosts.get(host)
                    if cred:
                        current['user'] = cred['username']
                        current['passw'] = cred['password']
                elif count > 1:
                    # Any more prameters need to update origin database.
                    current['user'] = arg.split()[1]
                    if count > 2:
                        # updat the password too.
                        current['passw'] = arg.split()[2]
                    Config().insert_host(current)
                Config().current = current
        except ValueError:
            print(self.__doc__)


    def __init__(self, arg=None):
        # No more sub commands, so return the function directly
        self.subs = self.host


class User(subcmd.SubCmd):
    """ user [name_to_be_changed]
        user [name]: assign username for current host
    """
    def do_user(self, arg):
        try:
            if len(arg.split()) == 0:
                raise ValueError
            if len(arg.split()) > 0:
                current = Config().current
                user = arg.split()[0]
                current['user'] = user
                Config().current = current
                Config().insert_host(current)
        except ValueError:
            print(self.__doc__)

    def __init__(self, arg=None):
        # No more sub commands, so return the function directly
        self.subs = self.do_user


class Passw(subcmd.SubCmd):
    """ passw [name_to_be_changed]
        passw [name]: assign password for current host
    """
    def do_passw(self, arg):
        try:
            if len(arg.split()) == 0:
                raise ValueError
            if len(arg.split()) > 0:
                current = Config().current
                passw = arg.split()[0]
                current['passw'] = passw
                Config().current = current
                Config().insert_host(current)
        except ValueError:
            print(self.__doc__)

    def __init__(self, arg=None):
        # No more sub commands, so return the function directly
        self.subs = self.do_passw

