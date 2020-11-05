#!/usr/bin/env python3
from __future__ import annotations

import os, sys
import json
import logging
from typing import List
from abc import ABC, abstractmethod

class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass



class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass



class Config:
    """ Singleton class to save the Config.
        Inner class is the real only one instance.
    """

    CONFIGFN=".qsmcli.json"
    HISTORYFN=".qsmcli.history"

    class __Config(Subject):
        _observers: List[Observer] = []
        """
        List of subscribers. In real life, the list of subscribers can be stored
        more comprehensively (categorized by event type, etc.).
        """
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
            self.notify()

        def load(self):
            try:
                with open(self.storefn, 'r') as json_file:
                    config=json.load(json_file)
                    if isinstance(config, dict):
                        self.current = config.get('current')
                        if not isinstance(self.current, dict):
                            self.current = {'host':"", 'user': "", 'passw': ""}

                        self.hosts = config.get('hosts')
                        if not isinstance(self.hosts, dict):
                            self.hosts = {}
            except FileNotFoundError:
                self.current={'host':'', 'user':'', 'passw':''}
                self.hosts={}

            
        def __str__(self):
            return repr(self)


        def attach(self, observer: Observer) -> None:
            logging.info("Subject: Attached an observer.")
            self._observers.append(observer)

        def detach(self, observer: Observer) -> None:
            self._observers.remove(observer)

        """
        The subscription management methods.
        """
        def notify(self) -> None:
            """
            Trigger an update in each subscriber.
            """
            logging.info("Subject: Notifying observers...")
            for observer in self._observers:
                observer.update(self.current)




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

    def insert_host(self, host):
        """ If all the host, users & password is not empty
            Insert a host or update to the hosts database.
        """
        if host['host'] and host['user'] and host['passw']:
            hosts = Config().hosts
            cred = {'username': host['user'], 'password': host['passw']}
            hosts[host['host']] = cred
            Config().hosts = hosts


    @classmethod
    def getHistoryFnPath(cls):
        return os.path.dirname(os.path.realpath(sys.argv[0])) + '/' + Config.HISTORYFN

    @classmethod
    def getConfigFnPath(cls):
        return os.path.dirname(os.path.realpath(sys.argv[0])) + '/' + Config.CONFIGFN




