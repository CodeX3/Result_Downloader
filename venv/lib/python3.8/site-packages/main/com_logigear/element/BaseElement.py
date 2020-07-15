'''
Created on Jul 19, 2017

@author: khoi.ngo
'''
from ..driver.driver_manager import DriverManager
import threading


class BaseElement():
    # private final Locator locator;
    _instance = None
    _timeOutInSeconds = 30
    _locator = None
    locator = "{{By: {}, Value: {}}}"

    lock = threading.RLock()

    def getLocator(self):
        return self._locator

    def __init__(self, locator):
        self._locator = locator

    def get_web_element(self):
        self.lock.acquire()
        if (self._instance is None):
            # two or more threads might be here!!!
            self._instance = DriverManager.get_web_driver().find_element(self._locator)
        self.lock.release()
        return self._instance

    def reload(self):
        self._instance = DriverManager.get_web_driver().findElement(self._locator)

    def click(self):
        self.get_web_element().click()

    def submit(self):
        self.get_web_element().submit()

    def clear(self):
        self.get_web_element().clear()

    def send_keys(self, value):
        self.get_web_element().send_keys(*value)

    def type(self, value):
        self.clear()
        self.send_keys(value)

    def get_tag_name(self):
        return self.get_web_element().get_tag_name()

    def get_attribute(self, name):
        return self.get_web_element().get_attribute(name)

    def is_selected(self):
        return self.get_web_element().is_selected()

    def is_enabled(self):
        return self.get_web_element().is_enabled()

    def get_text(self):
        return self.get_web_element().text()

    def find_element(self, by):
        return self.get_web_element().find_element(by)




