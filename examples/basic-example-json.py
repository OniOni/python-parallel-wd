import unittest
from selenium import webdriver
import copy

import sys, os

PATH = lambda f: os.path.join(os.path.dirname(os.path.abspath(__file__)), f)
                              
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(path)
import wd.parallel


class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        self.drivers = wd.parallel.Remote()
        self.drivers.load_config_file(os.path.join(PATH("config.json")))
        

    @wd.parallel.multiply
    def test_sauce(self):
        print "start"
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertTrue("I am a page title - Sauce Labs" in self.driver.title);
        print "title is ok"
        
        self.driver.find_element_by_id('comments').send_keys('Hello! I am some example comments. I should appear in the page after you submit the form')
        self.driver.find_element_by_id('submit').click()

        comments = self.driver.find_element_by_id('your_comments')
        self.assertTrue('Your comments: Hello! I am some example comments. I should appear in the page after you submit the form' in comments.text)
        print "Comments are ok"
        
        body = self.driver.find_element_by_xpath('//body')
        self.assertFalse('I am some other page content' in body.text)
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('I am some other page content' in body.text)
        print "Body is ok"

    @wd.parallel.multiply
    def tearDown(self):
        print 'quit'
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

