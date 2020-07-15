# -*- coding: utf-8 -*-
import sys
import logging

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from selenium.common.exceptions import InvalidSessionIdException

log = logging.getLogger(__name__)


class DriverFactory:
    """This class parse the config dict to generate the list of Driver
    """

    @classmethod
    def get_web_drivers(cls, conf):
        web_drivers = []
        global_capabilities = conf.get('global_capabilities', None)
        for driver in conf['drivers']:
            if 'class' not in driver:
                raise ValueError("missing `class` key in driver config %r",
                                 driver)
            index = driver['class'].rfind('.')
            module_name = driver['class'][:index]
            class_name = driver['class'][index + 1:]
            if module_name not in sys.modules:
                __import__(module_name)
            module = sys.modules[module_name]
            driver_class = getattr(module, class_name)
            web_drivers.extend(driver_class.get_web_drivers(
                driver, global_capabilities=global_capabilities))
        return web_drivers


class Driver(object):
    """Abstract class to define and ensure to expose uniform public API

    We mainly recommand to use `get_web_drivers` class method to instanciate
    Drivers. For instance remote webdrivers that use service like selenium Grid
    will return multiple instance of Driver..
    """
    __metaclass__ = ABCMeta

    _name = None
    _web_driver = None
    _capabilities = None
    conf = None

    global_capabilities = None
    """Capabilities shared between drivers"""

    @classmethod
    def get_web_drivers(cls, conf, global_capabilities=None):
        """Class method to prepare Driver(s) instance according current
        Driver class and given settings.

        :param conf: a dict that contains the Driver configuration
        :param global_capabilities: Capabilities shared over Drivers
                                    configuration
        :return: a list of Driver
        """
        return [cls(conf, global_capabilities=global_capabilities)]

    def __init__(self, conf, global_capabilities=None, name=None):
        """

        :param conf: configuration for the given driver, overwrite global
                     capabilities
        :param global_capabilities: capabilities shared over drivers
        :return: An instance of Driver class
        """
        self.conf = conf
        self._capabilities = (deepcopy(global_capabilities) if
                              global_capabilities else {})
        self._capabilities.update(conf.get('capabilities', {}))
        if name:
            self._name = name

    @property
    def name(self):
        """
        :return: the technical name that describe the related webdriver
        """
        return self._name

    @property
    def selenium(self):
        """Get the instance of webdriver, it starts the browser if the
        webdriver is not yet instantied

        :return: a `selenium instance <http://selenium-python.readthedocs.org/
        api.html#module-selenium.webdriver.remote.webdriver>`
        """
        if not self._web_driver:
            self._web_driver = self._start_driver()
        return self._web_driver

    def quit(self):
        """Prefer this way to ``quit()`` a selenium to properly re-open the
        browser in case it was closed
        """
        if self._web_driver:
            try:
                self._web_driver.quit()
            except InvalidSessionIdException as err:
                # According the web driver self._web_driver.close() properly
                # quit the webdriver
                log.warning(
                    "Something goes wrong while quit the driver %r", err
                )
            finally:
                self._web_driver = None

    @abstractmethod
    def _start_driver(self):
        """Abstract method that MUST be set un sub class
        :return: the WebDriver instance
        """
