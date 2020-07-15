"""
Created on Jul 25, 2017

@author: khoi.ngo
"""
from ...element.BaseElement import BaseElement
from selenium.webdriver.common.by import By


class Label(BaseElement):
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
        return Label((By.CSS_SELECTOR, selector))
    
    @staticmethod
    def xpath(xpath_expression):
        return Label((By.XPATH, xpath_expression))
    
    @staticmethod
    def id(id_value):
        return Label((By.ID, id_value))
    
    @staticmethod
    def name(name):
        return Label((By.NAME, name))

    @staticmethod
    def link_text(text):
        return Label((By.LINK_TEXT, text))
    
    def get_text(self):
        return BaseElement.get_text(self)



