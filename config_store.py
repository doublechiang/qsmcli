#!/usr/bin/env python3

import os, sys
import json


class ConfigStore:

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


    def __init__(self):
        self.dict=dict()
