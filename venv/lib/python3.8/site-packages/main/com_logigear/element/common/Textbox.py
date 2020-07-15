"""
Created on Jul 25, 2017

@author: khoi.ngo
"""
from ...element.BaseElement import BaseElement
from selenium.webdriver.common.by import By


class Textbox(BaseElement):
    """
    classdocs
    """


    def __init__(self, locator):
        """
        Constructor
        """
        BaseElement.__init__(self, locator)

    @staticmethod
    def css_selector(selector):
        return Textbox((By.CSS_SELECTOR, selector))
    
    @staticmethod
    def xpath(xpath_expression):
        return Textbox((By.XPATH, xpath_expression))
    
    @staticmethod
    def id(id_value):
        return Textbox((By.ID, id_value))
    
    @staticmethod
    def name(name):
        return Textbox((By.NAME, name))

    @staticmethod
    def link_text(text):
        return Textbox((By.LINK_TEXT, text))
    
    def get_text(self):
        return BaseElement.get_text(self)
    
    def send_keys(self, value):
        BaseElement.send_keys(self, value)



