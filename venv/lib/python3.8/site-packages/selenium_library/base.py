#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


class Base:
    ''' Base selenium

    Example:
        from selenium_library import Base

        session = Base(headless=False)
        session.open('https://www.google.de')
        input = session.element('[name="q"]')
        session.click(input)
        session.send_keys(input, 'pipi')
    '''
    def __init__(
        self,
        options=None,
        browser='chrome',
        headless=True,
        window_width=1920,
        window_height=1080
    ):
        '''
        Init session vars

        Args:
        browser (str): Browser name
        headlesss (boolean): Hide browser
        window_width (int): Window width
        window_height (int): Window height
        '''
        self.browser = browser
        self.headless = headless
        self.options = options
        self.window_width = window_width
        self.window_height = window_height
        self.launch_browser()

    def launch_browser(self):
        '''Launch browser and create a session'''
        if self.browser == 'firefox':
            options = FirefoxOptions()
        else:
            options = ChromeOptions()

        if self.headless:
            options.add_argument('--headless')

        if self.options:
            for option in self.options:
                options.add_argument(option)

        window_size = '--window-size={},{}'.format(
            self.window_width,
            self.window_height
        )
        options.add_argument(window_size)

        if self.browser == 'firefox':
            self.session = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                firefox_options=options
            )
        elif self.browser == 'opera':
            self.session = webdriver.Opera(
                executable_path=OperaDriverManager().install(),
                options=options
            )
        else:
            self.session = webdriver.Chrome(
                ChromeDriverManager().install(),
                chrome_options=options
            )

    def open(self, url):
        '''Open a new url in the session'''
        self.session.get(url)

    def get_url(self):
        '''Get the current url from the session

        Returns (str): Current url
        '''
        return self.session.current_url

    def element(self, selector):
        ''' Try to find an element in dom

        Returns [None]: Element or None
        '''
        try:
            return self.session.find_element_by_css_selector(selector)
        except Exception:
            pass

    def elements(self, selector):
        ''' Try to find every element in dom
            If there is no element it returns None

        Args:
            selector (str): DOM selector


        Returns [None, list]: List of elements or None
        '''
        elements_list = self.session.find_elements_by_css_selector(selector)
        return (elements_list if len(elements_list) > 0 else None)

    def click(self, selector_or_element):
        '''Try to click on an element

        Args:
            selector_or_element [str, WebElement]
        '''
        el = None
        if type(selector_or_element) == 'str':
            el = self.element(selector_or_element)

        if isinstance(el, WebElement):
            el.click()

    def get_text(self, selector_or_element):
        '''Try to get text

        Args:
            selector_or_element [str, WebElement]

        Returns (str): Text from an element
        '''
        el = None
        if type(selector_or_element) == 'str':
            el = self.element(selector_or_element)

        if isinstance(el, WebElement):
            return el.text


    def send_keys(self, selector_or_element, keys):
        ''' Send keys to an element

        Args:
            selector_or_element [str, WebElement]
            keys (str): Keys to send
        '''
        el = None
        if type(selector_or_element) == 'str':
            el = self.element(selector_or_element)

        if isinstance(el, WebElement):
            el.send_keys(keys)

    def clear_keys(self, selector_or_element):
        '''Clear keys from element

        Args:
            selector_or_element [str, WebElement]
        '''
        if type(selector_or_element) == 'str':
            el = self.element(selector_or_element)

        if isinstance(el, WebElement):
            el.clear()

    def wait(self, time=1, is_random=False, min=1, max=10):
        '''Wait a specific time or random

        Args:
            time (int): Time to stop script
            is_random (boolean): Waits a random time if true
            min (int): Minium time to wait if random
            max (int): Max time to wait if random
        '''
        if is_random:
            time.sleep(random.randint(min, max))
        else:
            time.sleep(time)

    def close(self):
        ''' Close the current session '''
        self.session.close()

    def __enter__(self):
        '''Will be executed when this class will be created via ContextMenu'''
        return self

    def __exit__(self, *args):
        ''' Will be executed when this class will be closed via ContextMenu '''
        self.close()
