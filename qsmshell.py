#! /usr/bin/env python3

import sys
import os
import cmd2
import logging
import inspect

# local modules
from config import Config
from interface import Interface
from nic import Nic
from mac import Mac
from cpld import Cpld
from fan import Fan
from service import Service
from install import Install
from version import Version
from me import Me
from ipmi import Ipmi

class QsmShell(cmd2.Cmd):

    intro = 'Type help or ? to list the command.\n'
#    prompt = GlobalVars.host + ":" +  GlobalVars.username + "(" + GlobalVars.password +")>"

    def emptyline(self):
        """ Disable the last command when hitting enter """
        pass

    def do_shell(self, line):
        """Run a shell command by use a ! prefix """
        print ("running shell command:", line)
        output = os.popen(line).read()
        print (output)
        self.last_output = output

    def do_exit(self, arg):
        """ exit from the shell """
        return True

    def setPrompt(self):
        QsmShell.prompt = "{}:{}({})>".format(self.env['host'], self.env['user'], self.env['passw'])

    def do_user(self, arg):
        """ user [name_to_be_changed]
            user [name]: assign the new password
        """
        if len(arg.split()) > 0:
            self.env['user'] = arg.split()[0]
            self.setPrompt()
            Config().current = self.env
            self.__update_hosts()

    def do_passw(self, arg):
        """ passw [name_to_be_changed]
            passw [name]: assign the new password
        """
        if len(arg.split()) > 0:
            self.env['passw'] = arg.split()[0]
            self.setPrompt()
            Config().current = self.env
            self.__update_hosts()

    def do_host(self, arg):
        """ host commands to switch the host ip.
            host [ip] [username] [password]: assign the new credentials
            if username and password are supplied, it will change the host/username/password in one command.
        """
        count = len(arg.split())
        if count > 0:
            host = arg.split()[0]
            self.env['host'] = host
            Config().current = self.env
            hosts = Config().hosts

            if count == 1:
                # if only host is provided, then check if host has been saved before
                # if exist, then use the previous user & passw
                cred = hosts.get(self.env['host'])
                if cred:
                    self.env['user'] = cred['username']
                    self.env['passw'] = cred['password']
            elif count > 1:
                # Any far more prameter need to update origin database.
                self.env['user'] = arg.split()[1]
                if count > 2:
                    # updat the password too.
                    self.env['passw'] = arg.split()[2]
                self.__update_hosts()
        self.setPrompt()

    def __update_hosts(self):
        """ If all the host, users & password is not empty, update the configuration.
        """
        if self.env['host'] and self.env['user'] and self.env['passw']:
            hosts = Config().hosts
            cred = {'username': self.env['user'], 'password': self.env['passw']}
            hosts[self.env['host']] = cred
            Config().hosts = hosts

    def do_EOF(self, arg):
        return True

    def regCmds(self, cmds):
        """ Register all of the support commands into cmd2
        """
        for cmd in cmds:
            self.regCmd(cmd)

    def regCmd(self, cmd):
        """ based cmd name to register the method with 
            do_xxx
            help_xxx
            complete_xxx 
        """
        funcdef = """def do_{}(self, arg):
                {}().run(arg)""".format(cmd, cmd.capitalize())
        assign = "QsmShell.do_{0} = do_{0}".format(cmd)
        exec(funcdef)
        exec(assign)
        funcdef = "def help_{}(self): print({}.__doc__)".format(cmd, cmd.capitalize())
        assign = "QsmShell.help_{0} = help_{0}".format(cmd)
        exec(funcdef)
        exec(assign)
        funcdef = """def complete_{}(self, text, line, begidx, endidx):
                        return [ i for i in {}().supported_cmds if i.startswith(text)]
                        """.format(cmd, cmd.capitalize())
        assign = "QsmShell.complete_{0} = complete_{0}".format(cmd)
        exec(funcdef)
        exec(assign)

    def __init__(self, **kwarg):
        """ load the shell environment from config
        """
        self.env = Config().current
        self.setPrompt()
        super().__init__(**kwarg)


