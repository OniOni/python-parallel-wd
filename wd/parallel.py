from selenium import webdriver 
import unittest
import json
import multiprocessing

class Remote(object):
    """
    """
    
    def __init__(self, desired_capabilities=None, command_executor=None):
        """
        
        Arguments:
        - `desired_capabilities`: Array of desired_capabilities
        - `command_executor`: Id string
        """

        self._command_executor = command_executor

        #Set up all webdrivers
        if desired_capabilities != None and command_executor != None:
        #    self.__create_drivers(desired_capabilities)
            self._desired_capabilities = desired_capabilities
        
        
    def load_config_file(self, file):
        """Open json file and load config from it
        
        Arguments:
        - `file`: json file containing conf
        """
        fd = open(file)
        conf = json.load(fd)
        self._command_executor = self.__build_command_executor(conf['remote'])

        #self.__create_drivers(conf['desired'])
        self._desired_capabilities = conf['desired']

    def __build_command_executor(self, remote):
        return str('http://'+remote['username']+':'+remote['accessKey']+'@'+\
            remote['host']+':'+str(remote['port'])+'/wd/hub')

    def __create_drivers(self, desired_capabilities):
        """Create  webdrives from desired capabilities
        
        Arguments:
        - `self`:
        - `desired_capabilities`:
        """
        for d in desired_capabilities:
            self._drivers += [webdriver.Remote(desired_capabilities=d,
                                               command_executor=self._command_executor)]
    def register(self, wd):
        try:
            self._drivers += [wd]
        except AttributeError as e:
            self._drivers = [wd]

        print repr(len(self._drivers)) + ' drivers registered'
            
            
def multiply(test):
    """Make test run in mutiple browsers
    """

    class SubTest(unittest.TestCase):
        def __init__(self, driver=None):
            self.driver = driver
            self.driver.implicitly_wait(30)

    def thread_func(f, dc=None, ce=None, driver=None, queue=None):

        if driver == None and dc != None:
            driver = webdriver.Remote(desired_capabilities=dc,
                                      command_executor=ce)
            if queue != None:
                queue.put(driver)

        print 'Launching test'
        f(SubTest(driver))
        
    def wrapper(*args, **kwargs):
        threads = []
        queue = multiprocessing.Queue(len(args[0].drivers._desired_capabilities) + 1)
        i = 0
        nb_d = 0

        try:
            print repr(len(args[0].drivers._drivers)) + ' drivers.'
            for d in args[0].drivers._drivers:
                t = multiprocessing.Process(target=thread_func, args=(test,), kwargs={'driver': d})
                t.start()
                threads += [t]
                i += 1
                print "One thread started | " +repr(i)+ " threads running"
                
        except AttributeError:
            for c in args[0].drivers._desired_capabilities:
                t = multiprocessing.Process(target=thread_func, args=(test,),
                                            kwargs={'dc': c,
                                             'ce': args[0].drivers._command_executor,
                                             'queue': queue
                                                })
                t.start()
                threads += [t]
                i += 1
                print "One thread started | " +repr(i)+ " threads running"

            while nb_d < len(args[0].drivers._desired_capabilities):
                driver = queue.get(block=True)
                args[0].drivers.register(driver)
                nb_d += 1

        for t in threads:
            t.join()
            i -= 1
            print "One thread stopped | " +repr(i)+ " threads running"
            
        # o = SubTest(d)
        # test(o)
            
    return wrapper

