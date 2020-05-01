#!/usr/bin/env python3

import os, sys
import json
import logging

class Config:
    """ Singleton class to save the Config.
        Inner class is the real only one instance.
    """

    CONFIGFN=".qsmcli.json"
    HISTORYFN=".qsmcli.history"

    class __Config:
        def __init__(self):
            """ Configuration
                current setting to store the host, username & password
                hosts saved successfully historied paired.
            """
            self.storefn = Config.getConfigFnPath()

            # Load the configuration file file
            self.load()

        def save(self):
            with open(self.storefn, 'w') as json_file:
                config = dict()
                config['current'] = self.current
                config['hosts'] = self.hosts
                json.dump(config, json_file)

        def load(self):
            with open(self.storefn, 'r') as json_file:
                config=json.load(json_file)
                if isinstance(config, dict):
                    self.current = config.get('current')
                    if not isinstance(self.current, dict):
                        self.current = {'host':"", 'user': "", 'passw': ""}

                    self.hosts = config.get('hosts')
                    if not isinstance(self.hosts, dict):
                        self.hosts = {}
            
        def __str__(self):
            return repr(self)
    instance = None
    # outer class definition below
    def __init__(self):
        if not Config.instance:
            Config.instance = Config.__Config()

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name, value):
        setattr(self.instance, name, value )
        self.instance.save()

    @classmethod
    def getHistoryFnPath(cls):
        return os.path.dirname(os.path.realpath(sys.argv[0])) + '/' + Config.HISTORYFN

    @classmethod
    def getConfigFnPath(cls):
        return os.path.dirname(os.path.realpath(sys.argv[0])) + '/' + Config.CONFIGFN




