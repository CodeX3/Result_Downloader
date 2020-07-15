# -*- coding: utf-8 -*-
"""Local driver to launch browser on the current computer.

While instantiate a webdriver you can request for different `capabilities
<https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities>`_, to
change available behavior of the browser.
"""
from selenium_configurator.driver import Driver
from selenium import webdriver


class Firefox(Driver):
    """Local Firefox webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Firefox',
            'capabilities': {
                ...
            }
        }

    `Specific capabilities <https://github.com/SeleniumHQ/selenium/wiki/
    DesiredCapabilities#webdriver>`_
    """
    _name = "local_firefox"

    def _start_driver(self):
        return webdriver.Firefox(**self._capabilities)


class Chrome(Driver):
    """Local Chrom/Chromium webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Chrome',
            'capabilities': {
                ...
            }
        }

    `Specific capabilities <https://sites.google.com/a/chromium.org/
    chromedriver/capabilities>`_
    """
    _name = "local_chrome"

    def _start_driver(self):
        return webdriver.Chrome(**self._capabilities)


class Ie(Driver):
    """Local Internet Explorer webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Ie',
            'capabilities': {
                ...
            }
        }

    `Specific capabilities <https://github.com/SeleniumHQ/selenium/wiki/
    DesiredCapabilities#ie-specific>`_
    """
    _name = "local_IE"

    def _start_driver(self):
        return webdriver.Ie(**self._capabilities)


class Opera(Driver):
    """Local Opera webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Opera',
            'capabilities': {
                ...
            }
        }
    """
    _name = "local_Opera"

    def _start_driver(self):
        return webdriver.Opera(**self._capabilities)


class Safari(Driver):
    """Local Safari webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Safari',
            'capabilities': {
                ...
            }
        }

    `Specific capabilities <https://github.com/SeleniumHQ/selenium/wiki/
    DesiredCapabilities#safari-specific>`_
    """
    _name = "local_Safari"

    def _start_driver(self):
        return webdriver.Safari(**self._capabilities)


class Phantomjs(Driver):
    """Local phantomjs webdriver

    Configuration settings::

        {
            'class': 'selenium_configurator.drivers.local.Phantomjs',
            'capabilities': {
                ...
            }
        }

    """
    _name = "local_phantomjs"

    def _start_driver(self):
        return webdriver.PhantomJS(**self._capabilities)
