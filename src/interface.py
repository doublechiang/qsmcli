#!/usr/bin/env python3

class Interface():
    """ Store the lan interface attributes.
    """ 
    def format(self):
        # return the parameter for ipmitool.
        str = ""
        if self.host and self.user and self.passw:
            str = "-H {} -U {} -P {} ".format(self.host, self.user, self.passw)
        return str

    def __init__(self, *argv, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
