"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from ...driver.driver import Driver
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class DesktopInternetExplorerDriver(Driver):
    """
    Init desktop Internet explorer driver.
    """


    def __init__(self, properties):
        """
        Constructor
        """
        Driver.__init__(self, properties)
        if ((properties.get_remote_url() is None) or (properties.get_remote_url() == "")):
            executable_path = properties.get_executable_path()
            print("Picking up IE executable at " + executable_path)
            driver = webdriver.Ie(executable_path)
            self.set_web_driver(driver)
        else:
            capabilities = DesiredCapabilities.INTERNETEXPLORER.copy()
            capabilities['platform'] = properties.get_platform()
            capabilities['version'] = properties.get_browser_version()
            webdriver.Remote(command_executor=properties.get_remote_url(), desired_capabilities=capabilities)