#! /usr/bin/env python3

import sys
import os
import cmd2
import logging
import inspect

# local modules
from interface import Interface
from nic import Nic
from mac import Mac
from cpld import Cpld
from fan import Fan
from service import Service
from install import Install
from version import Version
from me import Me
from fw import Fw
from ipmi import Ipmi
from host import Host, User, Passw
from config import Config

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
                {}().run(arg, self)""".format(cmd, cmd.capitalize())
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
        self.setPrompt(Config().current)
        super().__init__(**kwarg)

    def setPrompt(self, env):
        """
        setup the prompt shell by providing a dict.
        """
        self.prompt = "{}:{}({})>".format(env.get('host'), env.get('user'), env.get('passw'))



