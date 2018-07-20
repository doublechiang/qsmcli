#!/usr/bin/env python3

import os, sys
import configparser

TOKEN_USERNAME="username"
TOKEN_PASSWORD="password"
TOKEN_HOST="host"
CONFIG_FILE=".qsmcli.ses"

class GlobalVars:

    username=""
    password=""
    host=""

    @staticmethod
    def save(cfg_filename=CONFIG_FILE):
        config = configparser.ConfigParser()
        config.add_section('global')
        config.set('global', TOKEN_USERNAME, GlobalVars.username)
        config.set('global', TOKEN_PASSWORD, GlobalVars.password)
        config.set('global', TOKEN_HOST, GlobalVars.host)

        with open(cfg_filename, 'w') as cfgfile:
            config.write(cfgfile)
            cfgfile.close()

#        print("cfg file saved")

    @staticmethod
    def load(cfg_filename=CONFIG_FILE):
        try:
            config =  configparser.ConfigParser()
            config.read(cfg_filename)
            GlobalVars.username= config.get('global', TOKEN_USERNAME)
            GlobalVars.password= config.get('global', TOKEN_PASSWORD)
            GlobalVars.host= config.get('global', TOKEN_HOST)
#            print("Loading configuration.....")
            config.close()
        except:
            pass


    @staticmethod
    def host_access():
        return "ipmitool -H " + GlobalVars.host + " -U " + GlobalVars.username + " -P " + GlobalVars.password
