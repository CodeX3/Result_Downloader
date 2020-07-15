# -*- coding: utf-8 -*-
from copy import deepcopy
from selenium_configurator.driver import Driver
from selenium import webdriver


class Grid(Driver):
    """Grid Driver class to use over browsers over a
    `Selenium Grid <TODO LINK>`_

    It give you the availybility to request multiple browsers against one Grid
    server.

    Configuration settings to get 1 Chrome and 1 Firefox over a Grid service::

        conf = {
            'class': 'selenium_configurator.drivers.remote.Grid',
            'capabilities': {
                # Capabilities shared with request browser and overload
                # general capabilities
            },
            "request_drivers": [
                {
                    "browserName": "firefox",
                    "platform": "LINUX",
                    "version": "",
                    # other capabilities
                },
                {
                    "browserName": "chrome",
                    "platform": "LINUX",
                    "version": "",
                },
            ]
        }
        from selenium_configurator.driver.remote import Grid
        driver_list = Grid.get_web_drivers(conf)

    `Available request drivers capabilities <https://github.com/SeleniumHQ/
    selenium/wiki/JsonWireProtocol>`_
    """

    @classmethod
    def get_web_drivers(cls, conf, global_capabilities=None):
        """Prepare 1 selenium driver instance per request browsers

        :param conf:
        :param global_capabilities:
        :return:
        """
        web_drivers = []
        if not global_capabilities:
            global_capabilities = {}
        else:
            global_capabilities = deepcopy(global_capabilities)
        grid_conf = deepcopy(conf)
        grid_conf.pop('class', None)
        request_drivers = grid_conf.pop('request_drivers', [])
        capabilities = grid_conf.pop('capabilities', {})
        global_capabilities.update(capabilities)
        for browser_req in request_drivers:
            name = 'grid'
            name = '%s_%s' % (name, browser_req.get('browserName'))
            name = '%s_%s' % (name, browser_req.get('version', 'lastest'))
            name = '%s_%s' % (name, browser_req.get('platform', 'ANY'))
            web_drivers.append(Grid(grid_conf, browser_req, name=name,
                                    global_capabilities=global_capabilities))
        return web_drivers

    def __init__(
        self, grid_conf, desired_capabilities, global_capabilities=None,
        name=None
    ):
        """Init grid driver configurationn, in main case you would probably
        prefer use get_web_drivers method to instantiate driver class
        from the configuration.

        :param grid_conf: config related to the Grid itself
        :param desired_capabilities: desired browser against that grid
        :param global_capabilities: global capabilities request overs all
                                    browsers
        :param name: name of the driver
        """
        capab = deepcopy(global_capabilities) if global_capabilities else {}
        capab.update(desired_capabilities)
        self._capabilities = deepcopy(grid_conf)
        self._capabilities.update({
            'desired_capabilities': capab
        })
        if name:
            self._name = name

    def _start_driver(self):
        return webdriver.Remote(**self._capabilities)
