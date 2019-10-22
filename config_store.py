#!/usr/bin/env python3

import os, sys
import json


class ConfigStore:

    CONFIG_FILE=".qsmcli.json"

    def setValue(self, key, value):
        self.dict[key] = value
    def getValue(self, key):
        return self.dict[key]

    def save(self, filename=None):
        if filename is None:
            filename=self.__get_config_file_path()

        with open(filename, 'w') as json_file:
            json.dump(self.dict, json_file)
            json_file.close()

    def load(self, filename=None):
        if filename is None:
            filename=self.__get_config_file_path()

        with open(filename, 'r') as json_file:
            self.dict=json.load(json_file)
            json_file.close()

    def __get_config_file_path(self):
        dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        config_file = dir + '/' + ConfigStore.CONFIG_FILE
        return config_file


    def __init__(self):
        self.dict=dict()
