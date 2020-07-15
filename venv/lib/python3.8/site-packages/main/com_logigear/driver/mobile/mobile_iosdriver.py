"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from selenium.webdriver import DesiredCapabilities
from ...driver.driver import Driver
from selenium import webdriver

class MobileIOSDriver(Driver):
    """
    classdocs
    """


    def __init__(self, properties):
        """
        Constructor
        """
        super(MobileIOSDriver, properties).__init__()
        capabilities = None;
        if (properties.get_browser_name() == "iPhone"):
            capabilities = DesiredCapabilities.IPHONE.copy()
        elif (properties.get_browser_name() == "iPad"):
            capabilities = DesiredCapabilities.IPAD.copy()
        capabilities['version'] = properties.get_version()
        webdriver.Remote(command_executor=properties.get_remote_url(), desired_capabilities=capabilities)
