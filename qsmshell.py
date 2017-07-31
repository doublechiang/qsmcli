#! /usr/bin/env python3

import cmd, sys
import os

from globalvars import GlobalVars
from sel import Sel
from sdr import Sdr
from ipmi import Ipmi

class QsmShell(cmd.Cmd):

    intro = 'Type help or ? to list the command.\n'
#    prompt = GlobalVars.host + ":" +  GlobalVars.username + "(" + GlobalVars.password +")>"


    def emptyline(self):
        """ Disable the last command when hitting enter """
        pass

    def do_shell(self, line):
        """Run a shell command"""
        print ("running shell command:", line)
        output = os.popen(line).read()
        print (output)
        self.last_output = output

    def do_sel(self, arg):
        """System event log: info list csv
            info: give information on the system log
            list: list system event log
            csv: csv <filename>, save the output to csv format"""
        sel = Sel(arg)
    def complete_sel(self, text, line, begidx, endidx):
        return [ i for i in Sel.supported_cmds() if i.startswith(text)]


    def do_sdr(self, arg):
        """Sensor Data Record command"""
        sdr = Sdr(arg)
    def complete_sdr(self, text, line, begidx, endidx):
        return [ i for i in Sdr.supported_cmds() if i.startswith(text)]

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
        """ ipmitool command
            redirect parameter suffix to ipmitool
        """
        ipmi = Ipmi(arg)

    def do_EOF(self, arg):
        return True




if __name__ == '__main__':
    if len(sys.argv) > 1:
        QsmShell.onecmd(' '.join(sys.argv[1:]))
    else:
        QsmShell().cmdloop()
