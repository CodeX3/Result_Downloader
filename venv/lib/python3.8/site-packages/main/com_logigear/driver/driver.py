"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import Select


class Driver(object):
    """
    classdocs
    """
    __driver = None
    __driver_properties = None

    def __init__(self, properties):
        """
        Constructor
        """
        self.set_driver_properties(properties)

    def get_web_driver(self):
        return self.__driver

    def get_driver_properties(self):
        return self.__driver_properties

    def set_web_driver(self, value):
        self.__driver = value

    def set_driver_properties(self, value):
        self.__driver_properties = value

    def get(self, url):
        self.get_web_driver().get(url)

    def get_current_url(self):
        return self.get_web_driver().get_current_url()

    def get_title(self):
        return self.get_web_driver().get_title()

    def find_elements(self):
        print("TODO")

    def find_element(self, by):
        wait = WebDriverWait(self.get_web_driver(), 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable(by))
        return element

    def find_select_element(self, by):
        return Select(self.find_element(by))

    def get_page_source(self):
        return self.get_web_driver().get_page_source()

    def close(self):
        self.get_web_driver().close()

    def quit(self):
        self.get_web_driver().quit()

    def get_window_handles(self):
        return self.get_web_driver().get_window_handles()

    def get_window_handle(self):
        return self.get_web_driver().get_window_handle()

    def switch_to(self):
        return self.get_web_driver().switch_to()

    def navigate(self):
        return self.get_web_driver().navigate()

    def manage(self):
        return self.get_web_driver().manage()

    def maximize(self):
        self.get_web_driver().manage().window().maximize()

    def log_start_action(self, msg):
        print("Executing: " + msg)

    def log_end_action(self, msg):
        print("Done: " + msg)

    def wait_for_page_title(self, title):
        print("TODO")
