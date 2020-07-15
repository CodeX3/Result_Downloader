# -*- coding: utf-8 -*-
from selenium_configurator.driver import DriverFactory
import yaml


class Configurator(object):
    """This Configurator class is the entry point to prepare a selenium
    web driver list from a configuration string, file or object.

    A short example to launch on a local Firefox would be::

        from selenium_configurator.configurator import Configurator

        configurator = Configurator(
            {
                'drivers': [
                    {
                        'class': 'selenium_configurator.drivers.local.Firefox',
                    }
                ],
            }
        )
        drivers = configuration.get_drivers()
        for driver in drivers:
            driver.selenium.get('https://anybox.fr/)
            driver.quit()

    """

    config = None

    def __init__(self, config):
        """

        :param config: dict describing the wishes selenium configuration
        """
        self.config = config
        self._control_values()

    def _control_values(self):
        if not isinstance(self.config, dict):
            raise ValueError(
                "config attribute should be a dict (given %r)", self.config
            )

    @classmethod
    def from_string(cls, yaml_conf):
        """Create a Configurator from a string that expected to be
         a ``yaml`` or ``json`` format.

        :param yaml_conf: A string
        :return: An instance of Configurator
        """
        return Configurator(yaml.safe_load(yaml_conf))

    @classmethod
    def from_file(cls, path):
        """ Create a Configurator from a ``.yaml`` or ``.json`` file

        :param path: to the config file
        :return: An instance of Configurator
        """
        return Configurator(yaml.safe_load(open(path)))

    def get_drivers(self):
        """Get the list of driver instance from the configuration description
        provide to that configurator class

        :return: A list of drivers instances that contains selenium
                 instance ready to start,
        """
        self._control_values()
        return DriverFactory().get_web_drivers(self.config)
