#!/usr/bin/env python3

import os, sys
import configparser
from config_store import ConfigStore

class GlobalVars:

    username=""
    password=""
    host=""
    KEY_USERNAME="username"
    KEY_PASSWORD="password"
    KEY_HOST="host"

    KEY_HOSTS="hosts"
    hosts=dict()

    @staticmethod
    def save(cfg_filename=None):

        config = ConfigStore()
        config.setValue(GlobalVars.KEY_USERNAME, GlobalVars.username)
        config.setValue(GlobalVars.KEY_PASSWORD, GlobalVars.password)
        config.setValue(GlobalVars.KEY_HOST, GlobalVars.host)
        config.setValue(GlobalVars.KEY_HOSTS, GlobalVars.hosts)
        config.save(cfg_filename)

#        print("cfg file saved")

    @staticmethod
    def load(cfg_filename=None):
        """ Load the configuration file from application path
        """

        try:
            config = ConfigStore()
            config.load(cfg_filename)
            GlobalVars.username = config.getValue(GlobalVars.KEY_USERNAME)
            GlobalVars.password = config.getValue(GlobalVars.KEY_PASSWORD)
            GlobalVars.host = config.getValue(GlobalVars.KEY_HOST)
            GlobalVars.hosts = config.getValue(GlobalVars.KEY_HOSTS)

        except:
            pass
    @staticmethod
    def update_host_credential(ip, user=None, password=None):
        """ If username & password are supplied, the same it as a pair.
        """
        if user is not None and password is not None:
            GlobalVars.hosts[ip] = {GlobalVars.KEY_USERNAME : user, GlobalVars.KEY_PASSWORD: password}

    @staticmethod
    def get_host_credential(ip):
        host = GlobalVars.hosts.get(ip)
        return host


    @staticmethod
    def host_access():
        return "ipmitool -H " + GlobalVars.host + " -U " + GlobalVars.username + " -P " + GlobalVars.password + " "
