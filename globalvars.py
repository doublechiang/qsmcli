#!/usr/bin/env python3

import os, sys
import configparser

TOKEN_USERNAME="username"
TOKEN_PASSWORD="password"
TOKEN_HOST="host"

class GlobalVars:

    username=""
    password=""
    host=""
    CONFIG_FILE=".qsmcli.ses"
    TOKEN_USERNAME="username"
    TOKEN_PASSWORD="password"
    TOKEN_HOST="host"

    @staticmethod
    def getAppConfigFile():
        dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        config_file = dir + '/' + GlobalVars.CONFIG_FILE
        return config_file


    @staticmethod
    def save(cfg_filename=None):
        if (cfg_filename is None):
            cfg_filename=GlobalVars.getAppConfigFile()
        config = configparser.ConfigParser()
        config.add_section('global')
        config.set('global', GlobalVars.TOKEN_USERNAME, GlobalVars.username)
        config.set('global', GlobalVars.TOKEN_PASSWORD, GlobalVars.password)
        config.set('global', GlobalVars.TOKEN_HOST, GlobalVars.host)

        with open(cfg_filename, 'w') as cfgfile:
            config.write(cfgfile)
            cfgfile.close()

#        print("cfg file saved")

    @staticmethod
    def load(cfg_filename=None):
        """ Load the configuration file from application path
        """
        if (cfg_filename is None):
            cfg_filename=GlobalVars.getAppConfigFile()

        try:
            config =  configparser.ConfigParser()
            config.read(cfg_filename)
            GlobalVars.username= config.get('global', GlobalVars.TOKEN_USERNAME)
            GlobalVars.password= config.get('global', GlobalVars.TOKEN_PASSWORD)
            GlobalVars.host= config.get('global', GlobalVars.TOKEN_HOST)
#            print("Loading configuration.....")
            config.close()
        except:
            pass


    @staticmethod
    def host_access():
        return "ipmitool -H " + GlobalVars.host + " -U " + GlobalVars.username + " -P " + GlobalVars.password
