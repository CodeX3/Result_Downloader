"""
Created on Jul 24, 2017

@author: khoi.ngo
"""


class DriverProperties(object):
    """
    classdocs
    """
    _browser_name = None
    _browser_version = ""
    _platform = None
    _platform_version = ""
    _remote_url = ""
    _executable_path = ""
    _element_wait_timeout = 1
    # only for mobile
    _device_name = ""
    # only for SauceLabs cloud
    _method_name = ""

    def __init__(self, *args):
        """
        Constructor
        """
        self._browser_name = args[0] #browser_name
        self._browser_version = args[1] #browser_version
        self._platform = args[2] #platform
        self._platform_version = args[3] #platform_version
        self._remote_url = args[4] #remote_url
        self._device_name = args[5] #device_name
        self._executable_path = args[6] #executable_path
        self._element_wait_timeout = args[7] #element_wait_timeout
        if len(args) == 9:
            self._method_name = args[8] #method_name

    def get_browser_name(self):
        return self._browser_name

    def get_browser_version(self):
        return self._browser_version

    def get_platform(self):
        return self._platform

    def get_platform_version(self):
        return self._platform_version

    def get_remote_url(self):
        return self._remote_url

    def get_executable_path(self):
        return self._executable_path

    def get_element_wait_time_out(self):
        return self._element_wait_timeout

    def get_device_name(self):
        return self._device_name

    def get_method_name(self):
        return self._method_name

    def set_browser_name(self, value):
        self._browser_name = value

    def set_browser_version(self, value):
        self._browser_version = value

    def set_platform(self, value):
        self._platform = value

    def set_platform_version(self, value):
        self._platform_version = value

    def set_remote_url(self, value):
        self._remote_url = value

    def set_executable_path(self, value):
        self._executable_path = value

    def set_element_wait_time_out(self, value):
        self._element_wait_timeout = value

    def set_device_name(self, value):
        self._device_name = value

    def set_method_name(self, value):
        self._method_name = value
