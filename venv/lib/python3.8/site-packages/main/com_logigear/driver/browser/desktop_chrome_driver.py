"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from ...driver.driver import Driver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import DesiredCapabilities


class DesktopChromeDriver(Driver):
    """
    Init desktop Chrome driver.
    """

    def __init__(self, properties):
        Driver.__init__(self, properties)
        if ((properties.get_remote_url() is None) or (properties.get_remote_url() == "")):
            executable_path = properties.get_executable_path()
            print("Picking up Chrome executable at " + executable_path)
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-logging")
#             prefs = {"download.default_directory": Driver_Windows.dir_name, "download.prompt_for_download": False, "safebrowsing.enabled": "false"}
#             chrome_options.add_experimental_option("prefs", prefs)
            driver = webdriver.Chrome(executable_path, chrome_options=chrome_options)
            self.set_web_driver(driver)
        else:
            capabilities = DesiredCapabilities.CHROME.copy()
            capabilities['platform'] = properties.get_platform()
            capabilities['version'] = properties.get_browser_version()
            webdriver.Remote(command_executor=properties.get_remote_url(), desired_capabilities=capabilities)
