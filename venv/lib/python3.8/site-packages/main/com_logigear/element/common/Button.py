"""
Created on Jul 24, 2017

@author: khoi.ngo
"""
from ...element.BaseElement import BaseElement
from selenium.webdriver.common.by import By


class Button(BaseElement):
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
        return Button((By.CSS_SELECTOR, selector))
    
    @staticmethod
    def xpath(xpath_expression):
        return Button((By.XPATH, xpath_expression))
    
    @staticmethod
    def id(id_value):
        return Button((By.ID, id_value))
    
    @staticmethod
    def name(name):
        return Button((By.NAME, name))

    @staticmethod
    def link_text(text):
        return Button((By.LINK_TEXT, text))
    
    def click(self):
        BaseElement.click()


