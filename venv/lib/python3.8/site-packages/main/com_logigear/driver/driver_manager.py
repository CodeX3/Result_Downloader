"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
import threading

from main.com_logigear.constant.constants import Platform, Browser

from ..driver.browser.desktop_chrome_driver import DesktopChromeDriver
from ..driver.browser.desktop_firefox_driver import DesktopFireFoxDriver
from ..driver.browser.desktop_internet_explorer_driver import DesktopInternetExplorerDriver
from ..driver.browser.desktop_safari_driver import DesktopSafariDriver
from ..driver.cloud.sauce_labs_driver import SauceLabsDriver
from ..driver.driver import Driver
from ..driver.mobile.mobile_android_driver import MobileAndroidDriver 
from ..driver.mobile.mobile_iosdriver import MobileIOSDriver 


class DriverManager(Driver):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """

    driver_map = {}
    lock = threading.RLock()
    
    @staticmethod
    def store_web_driver(driver):
        DriverManager.lock.acquire()
        DriverManager.driver_map[threading.get_ident()] = driver
        DriverManager.lock.release()

    @staticmethod
    def get_web_driver():
        DriverManager.lock.acquire()
        value = DriverManager.driver_map[threading.get_ident()]
        DriverManager.lock.release()
        return value

    @staticmethod
    def remove_web_driver(self):
        DriverManager.lock.acquire()
        del DriverManager.driver_map[threading.get_ident()]
        DriverManager.lock.release()

    @staticmethod
    def create_web_driver(driver_properties):
        try:
            DriverManager.lock.acquire()
            driver = None
            platform = driver_properties.get_platform()
            print("[STEP] Init driver on %s.\n" % (platform))
    
            if (driver_properties.get_remote_url().lower() =="saucelabs"):
                driver = SauceLabsDriver(driver_properties)
            else:
                if (platform.lower() == Platform.android):
                    driver = DriverManager.init_appium_android_driver(driver_properties)
                elif (platform.lower() == Platform.ios):
                    driver = DriverManager.init_appium_ios_driver(driver_properties)
                elif (platform.lower() == Platform.linux):
                    print("Not implement for {} yet.\n", platform)
                elif (platform.lower() == Platform.mac):
                    print("Not implement for {} yet.\n", platform)
                elif (platform.lower() == Platform.windows):
                    driver = DriverManager.init_selenium_driver(driver_properties)
            DriverManager.store_web_driver(driver)
            DriverManager.lock.release()
        except:
            print("[ERROR]: Cannot create Web driver for %s for %s.\n" %
                  (driver_properties.get_platform(), driver_properties.get_remote_url()))

    @staticmethod
    def init_selenium_driver(driver_properties):
        print("[STEP] Init Web driver for browser %s on %s.\n" %
              (driver_properties.get_browser_name(), driver_properties.get_platform()))

        browser_name = driver_properties.get_browser_name()
        if (browser_name.lower() == Browser.firefox):
            return DesktopFireFoxDriver(driver_properties)
        elif (browser_name.lower() == Browser.ie):
            return DesktopInternetExplorerDriver(driver_properties)
        elif (browser_name.lower() == Browser.chrome):
            return DesktopChromeDriver(driver_properties)
        elif (browser_name.lower() == Browser.safari):
            return DesktopSafariDriver(driver_properties)
        else:
            print("[ERROR]: Cannot create Local Local/Remote Web driver for browser %s on %s.\n" %
                  (driver_properties.get_browser_name(), driver_properties.get_platform()))
        return None

    @staticmethod
    def init_appium_android_driver(driver_properties):
        print("[STEP] Init Mobile Android driver for browser %s on %s.\n" %
              (driver_properties.get_browser_name(), driver_properties.get_remote_url()))
        return MobileAndroidDriver(driver_properties)
    
    @staticmethod
    def init_appium_ios_driver(driver_properties):
        print("[STEP] Init Mobile IOS driver for browser %s on %s.\n" %
              (driver_properties.get_browser_name(), driver_properties.get_remote_url()))
        return MobileIOSDriver(driver_properties)



    
    
    