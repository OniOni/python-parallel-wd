from selenium import webdriver 
import unittest
import json

class Remote(object):
    """
    """
    
    def __init__(self, desired_capabilities, command_executor):
        """
        
        Arguments:
        - `desired_capabilities`: Array of desired_capabilities
        - `command_executor`: Id string
        """
        
        self._command_executor = command_executor
        self._drivers = []

        #Set up all webdrivers
        self.__create_drivers(desired_capabilities)
        
    def load_config_file(self, file):
        """Open json file and load config from it
        
        Arguments:
        - `file`: json file containing conf
        """
        conf = json.load(file)


    def __build_command_executor(self, conf)
        return 'http://'+conf['username']+':'+conf['accessKey']+'@'+conf['host']+':'+conf['port']+'/wd/hub'

    def __create_drivers(self, desired_capabilities):
        """Create  webdrives from desired capabilities
        
        Arguments:
        - `self`:
        - `desired_capabilities`:
        """
        for d in desired_capabilities:
            self._drivers += [webdriver.Remote(desired_capabilities=d,
                                               command_executor=self._command_executor)]

            
            
def multiply(test):
    """Make test run in mutiple browsers
    """

    class SubTest(unittest.TestCase):
        def __init__(self, driver=None):
            self.driver = driver

    def wrapper(*args, **kwargs):
        for d in args[0].drivers._drivers:
            o = SubTest(d)
            test(o)
            
    return wrapper

