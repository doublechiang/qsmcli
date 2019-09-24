#! /usr/bin/env python3

import cmd, sys
import os

from globalvars import GlobalVars
from sel import Sel
from sdr import Sdr
from ipmi import Ipmi
from nic import Nic
from mac import Mac
from cpld import Cpld
from fan import Fan
from service import Service
from install import Install
from version import Version

class QsmShell(cmd.Cmd):

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

    def do_fan(self, arg):
        fan = Fan(arg)
    def help_fan(self):
        print(Fan.__doc__)
    def complete_fan(self, text, line, begidx, endidx):
        return [ i for i in Fan.supported_cmds() if i.startswith(text)]

    def do_service(self, arg):
        service = Service(arg)
    def help_service(self):
        print(Service.__doc__)
    def complete_serivce(self, text, line, begidx, endidx):
        return [ i for i in Service.supported_cmds() if i.startswith(text)]

    def do_sel(self, arg):
        sel = Sel(arg)
    def help_sel(self):
        print(Sel.__doc__)
    def complete_sel(self, text, line, begidx, endidx):
        return [ i for i in Sel.supported_cmds() if i.startswith(text)]

    def do_sdr(self, arg):
        sdr = Sdr(arg)
    def complete_sdr(self, text, line, begidx, endidx):
        return [ i for i in Sdr.supported_cmds() if i.startswith(text)]
    def help_sdr(self):
        print(Sdr.__doc__)

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
#        setPrompt(self)

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
            host [ip]: assign the new ip address
        """
        if arg:
            GlobalVars.host = arg.split()[0]
            QsmShell.setPrompt(self)
        else:
            print (GlobalVars.host)

    def do_ipmi(self, arg):
        ipmi = Ipmi(arg)
    def help_ipmi(self):
        print(Ipmi.__doc__)

    def do_mac(self, arg):
        mac = Mac(arg)
    def complete_mac(self, text, line, begidx, endidx):
        return [ i for i in Mac.supported_cmds() if i.startswith(text)]
    def help_mac(self):
        print (Mac.__doc__)

    def do_nic(self, arg):
        nic = Nic(arg)
    def help_nic(self):
        print(Nic.__doc__)
    def complete_nic(self, text, line, begidx, endidx):
        return [ i for i in Nic.supported_cmds() if i.startswith(text)]

    def do_cpld(self, arg):
        cpld = Cpld(arg)
    def complete_cpld(self, text, line, begidx, endidx):
        return [ i for i in Cpld.supported_cmds() if i.startswith(text)]
    def help_cpld(self):
        print (Cpld.__doc__)

    def do_install(self, arg):
        """ Install this application into system path
        """
        install=Install(arg)
    def help_install(self):
        print(Install.__doc__)

    def do_version(self, arg):
        """ Install this application into system path
        """
        print(Version())
    def help_version(self):
        print(Version.__doc__)


    def do_EOF(self, arg):
        return True




if __name__ == '__main__':
    if len(sys.argv) > 1:
        QsmShell.onecmd(' '.join(sys.argv[1:]))
    else:
        QsmShell().cmdloop()
