"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from selenium.webdriver import DesiredCapabilities
from ...driver.driver import Driver
from selenium import webdriver


class MobileAndroidDriver(Driver):
    """
    classdocs
    """


    def __init__(self, properties):
        """
        Constructor
        """
        super(MobileAndroidDriver, properties).__init__()
        capabilities = DesiredCapabilities.ANDROID.copy()
        capabilities['platform'] = properties.get_platform()
        capabilities['version'] = properties.get_version()
        capabilities['browserName'] = properties.get_browser_name()
        webdriver.Remote(command_executor=properties.get_remote_url(), desired_capabilities=capabilities)