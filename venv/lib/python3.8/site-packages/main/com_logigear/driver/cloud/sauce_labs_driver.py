"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from selenium import webdriver
from ...constant.constants import Browser, Platform
from ...driver.driver import Driver


class SauceLabsDriver(Driver):
    """
    classdocs
    """


    def __init__(self, properties):
        """
        Constructor
        """
        super(SauceLabsDriver, properties).__init__()

        username = "Partner_Logigear"; #System.getenv("SAUCE_USERNAME");
        accesskey = "7254afad-1964-44c7-b554-4db0ad1cf1cc"; #System.getenv("SAUCE_ACCESS_KEY");

#         authentication = SauceOnDemandAuthentication(username, accesskey);

        capabilities = {}
        
        # set desired capabilities to launch appropriate browser on Sauce
        if (properties.getBrowserName() == Browser.edge):
            capabilities['browserName'] = "MicrosoftEdge"
        elif (properties.getBrowserName() == Browser.ie):
            capabilities['browserName'] = "internet explorer"
        else:
            capabilities['browserName'] = properties.get_browser_name()

        if (properties.get_platform() == Platform.osx):
            capabilities['platform'] = "OS X " + properties.get_platform_version()
        else:
            capabilities['platform'] = properties.get_platform() + " " + properties.get_platform_version()

        capabilities['version'] = properties.get_browser_version()

        if ((properties.get_method_name() is not None) and (properties.get_method_name() != "")):
            capabilities['name'] = properties.get_method_name()

        # Launch remote browser and set it as the current thread
        webdriver.Remote(command_executor="https://" + username + ":" + accesskey + "@ondemand.saucelabs.com:443/wd/hub",
                desired_capabilities=capabilities)



