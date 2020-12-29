#! /usr/bin/env python3

import sys
import os
import cmd2
import logging
import inspect

# local modules
import subcmd
from subcmdfactory import SubCmdFactory
from config import Config, Observer, Subject



class QsmShell(cmd2.Cmd, Observer):

    intro = 'Type help or ? to list the command.\n'

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
                SubCmdFactory().Factory('{}').run(arg)""".format(cmd, cmd)
        assign = "QsmShell.do_{0} = do_{0}".format(cmd)
        exec(funcdef)
        exec(assign)
        funcdef = """def help_{}(self):
            print(SubCmdFactory().Factory('{}').__doc__)""".format(cmd, cmd)
        assign = "QsmShell.help_{0} = help_{0}".format(cmd)
        exec(funcdef)
        exec(assign)
        funcdef = """def complete_{}(self, text, line, begidx, endidx):
                        subcls = SubCmdFactory().Factory('{}')
                        return [ i for i in subcls.getSupportCmds() if i.startswith(text)]
                        """.format(cmd, cmd.capitalize())
        assign = "QsmShell.complete_{0} = complete_{0}".format(cmd)
        exec(funcdef)
        exec(assign)

    def __init__(self, **kwarg):
        """ load the shell environment from config
        """

        # Attach the shell to the config publisher.
        Config().attach(self)
        self.__setPrompt(Config().current)
        super().__init__(**kwarg)

    def __setPrompt(self, env):
        """
        setup the prompt shell by providing a dict.
        """
        self.prompt = "{}:{}({})>".format(env.get('host'), env.get('user'), env.get('passw'))

    def update(self, subject: Subject) -> None:
        self.__setPrompt(subject)



