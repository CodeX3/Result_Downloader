"""
Created on Jul 18, 2017

@author: khoi.ngo

Class define constant used for core selenium project
"""


class Browser():
    firefox = "firefox"
    ie = "internet_explorer"
    edge = "edge"
    safari = "safari"
    chrome = "chrome"

class LocatorType():
    id = "ID"
    name = "NAME"
    link_text = "LINK_TEXT"
    partial_link_text = "PARTIAL_LINK_TEXT"
    tag_name = "TAG_NAME"
    class_name = "CLASS_NAME"
    css = "CSS"
    xpath = "XPATH"

class Platform():
    windows = "windows"
    mac = "mac"
    android = "android"
    ios = "ios"
    linux = "linux"
    osx = "osx"
