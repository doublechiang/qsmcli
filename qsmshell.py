#! /usr/bin/env python3

import sys
import os
import cmd2
import logging

from globalvars import GlobalVars
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
        QsmShell.prompt = GlobalVars.host + ":" +  GlobalVars.username + "(" + GlobalVars.password +")>"

    def do_username(self, arg):
        """ username [name_to_be_changed]
            print the username
            username [name]: assign the new name to usernmae parameter"""
        if arg:
            GlobalVars.username = arg.split()[0]
            QsmShell.setPrompt(self)
        else:
            print (GlobalVars.username)

    def do_password(self, arg):
        """ password [name_to_be_changed]
            print the current password
            password [name]: assign the new password"""
        if arg:
            GlobalVars.password = arg.split()[0]
            QsmShell.setPrompt(self)
        else:
            print (GlobalVars.username)

    def do_host(self, arg):
        """ host [host_to_be_managed]
            print the current host ip address
            host [ip] [username] [password]: assign the new ip address
            if username and password are supplied, it will change the host/username/password in one command.
        """
        if arg:
            GlobalVars.host = arg.split()[0]
            # if a single host switch only command, chheck if history has credentials or not
            if len(arg.split()) == 1:
                credential = GlobalVars.get_host_credential(GlobalVars.host)
                if credential:
                    GlobalVars.username = credential.get(GlobalVars.KEY_USERNAME, "")
                    GlobalVars.password = credential.get(GlobalVars.KEY_PASSWORD, "")
            if len(arg.split()) > 1:
                GlobalVars.username = arg.split()[1]
            if len(arg.split()) > 2:
                GlobalVars.password = arg.split()[2]
            QsmShell.setPrompt(self)
            GlobalVars.update_host_credential(GlobalVars.host, GlobalVars.username, GlobalVars.password)


        else:
            print (GlobalVars.host)

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
        exec("from {} import {}".format(cmd, cmd.capitalize()))
        funcdef = "def do_{}(self, arg): {}().run(arg)".format(cmd, cmd.capitalize())
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


if __name__ == '__main__':
    if len(sys.argv) == 1:
        shell = QsmShell()
        shell.cmdloop()
