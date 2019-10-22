#!/usr/bin/env python3

import os, sys
import configparser
from config_store import ConfigStore

class GlobalVars:

    username=""
    password=""
    host=""
    TOKEN_USERNAME="username"
    TOKEN_PASSWORD="password"
    TOKEN_HOST="host"

    @staticmethod
    def save(cfg_filename=None):

        config = ConfigStore()
        config.setValue(GlobalVars.TOKEN_USERNAME, GlobalVars.username)
        config.setValue(GlobalVars.TOKEN_PASSWORD, GlobalVars.password)
        config.setValue(GlobalVars.TOKEN_HOST, GlobalVars.host)
        config.save(cfg_filename)

#        print("cfg file saved")

    @staticmethod
    def load(cfg_filename=None):
        """ Load the configuration file from application path
        """

        try:
            config = ConfigStore()
            config.load(cfg_filename)
            GlobalVars.username = config.getValue(GlobalVars.TOKEN_USERNAME)
            GlobalVars.password = config.getValue(GlobalVars.TOKEN_PASSWORD)
            GlobalVars.host = config.getValue(GlobalVars.TOKEN_HOST)

        except:
            pass

    @staticmethod
    def host_access():
        return "ipmitool -H " + GlobalVars.host + " -U " + GlobalVars.username + " -P " + GlobalVars.password + " "
