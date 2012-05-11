from selenium import webdriver 
import unittest
import json

class Remote(object):
    """
    """
    
    def __init__(self, desired_capabilities=None, command_executor=None):
        """
        
        Arguments:
        - `desired_capabilities`: Array of desired_capabilities
        - `command_executor`: Id string
        """

        print type(command_executor)
        self._command_executor = command_executor
        self._drivers = []

        #Set up all webdrivers
        if desired_capabilities != None and command_executor != None:
            self.__create_drivers(desired_capabilities)
        
    def load_config_file(self, file):
        """Open json file and load config from it
        
        Arguments:
        - `file`: json file containing conf
        """
        fd = open(file)
        conf = json.load(fd)
        self._command_executor = self.__build_command_executor(conf['remote'])

        self.__create_drivers(conf['desired'])

    def __build_command_executor(self, remote):
        return str('http://'+remote['username']+':'+remote['accessKey']+'@'+\
            remote['host']+':'+str(remote['port'])+'/wd/hub')

    def __create_drivers(self, desired_capabilities):
        """Create  webdrives from desired capabilities
        
        Arguments:
        - `self`:
        - `desired_capabilities`:
        """
        print self._command_executor
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

