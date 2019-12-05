#!/usr/bin/env python3

import os, sys
import subprocess
import logging

from globalvars import GlobalVars


class IpmiExec():
    """ IPMI command Object.
    """

    def __init__(self, arg=None, raw=[], channel=None, bridge=None, parser=None, setup=None):
        self.arg = arg
        self.raw=raw
        self.channel=channel
        self.bridge=bridge
        self.parser=parser
        self.setup=setup
        logging.debug("Ipmiexec.raw=%s, setup=%s", self.raw, self.setup)
        """
            params handle function input is a list of parameters
            output is the string format.
            if the number and format is wrong in the parameter, raise a ValueError.
        """

    def output(self):
        return self.stdout


    def run(self, arg=None, printcmd=True):
        logging.info("Ipmiexec.run() is called.")
        try:
            # if there is no existing command, we will composing one
            if self.arg is None:
                logging.debug("Ipmiexec.self.raw is %s", self.raw)
                if self.setup:
                    logging.debug("Calling setup %s", self.setup)
                    self.setup(self)
                if self.raw:
                    logging.debug("Composite cmds")
                    self.composite_cmds()

            cmd = GlobalVars.host_access() + self.arg
            if (printcmd):
                print(cmd)
            completed = subprocess.run(cmd.split(), universal_newlines = True, stdout=subprocess.PIPE)
            # print(completed.stdout.split())
            self.stdout=completed.stdout
            if (printcmd):
                print(self.stdout)

            # if we have parser, then using parser to process the output
            if callable(self.parser):
                self.parser(completed.stdout)
        except ValueError:
            # Capture nested value error, value error should printed the help document already, do nothgin here.``
            pass
        except AttributeError:
            logging.error("Attribute error caught")
        return self

    def composite_cmds(self):
        logging.debug("arg=%s, raw=%s", self.arg, self.raw)
        cmd = ""
        if self.bridge:
            cmd += "-t " + str(self.bridge)
        if self.channel:
            cmd += " -b " + str(self.channel) 
        self.arg = " raw " + self.raw
        return self

    def marshal_raw_cmds(self, *argv):
        """ Assemble the raw commands of get configuration.
            parameter argv: every arguments is a list with value for raw commands.
        """

        cmdbuf = ""
        #every argument is a digit list
        for list in argv:
            for val in list:
                cmdbuf += "0x%x " % val
        self.raw = cmdbuf
        return self

    def with_bridge(self, bridge):
        self.bridge= bridge
        return self

    def with_channel(self, channel):
        self.channel = channel
        return self
