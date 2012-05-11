import unittest
from selenium import webdriver
import parallelWd
import copy

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = []

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['version'] = '10'
        browser['platform'] = 'XP'
        browser['name'] = 'Python at Sauce 1/2'
        browser['tags'] = "Parallel"
        desired_capabilities += [browser]

        browser = copy.copy(webdriver.DesiredCapabilities.FIREFOX)
        browser['version'] = '10'
        browser['platform'] = 'LINUX'
        browser['name'] = 'Python at Sauce 2/2'
        browser['tags'] = "Parallel"
        desired_capabilities += [browser]

        self.drivers = parallelWd.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://msabourin:d37ee0b6-723b-4b4d-8933-52623541b998@ondemand.saucelabs.com:80/wd/hub"
        )
        
        #self.driver.implicitly_wait(30)

    @parallelWd.multiply
    def test_sauce(self):
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertTrue("I am a page title - Sauce Labs" in self.driver.title);
        self.driver.find_element_by_id('comments').send_keys('Hello! I am some example comments. I should appear in the page after you submit the form')
        self.driver.find_element_by_id('submit').click()

        comments = self.driver.find_element_by_id('your_comments')
        self.assertTrue('Your comments: Hello! I am some example comments. I should appear in the page after you submit the form' in comments.text)
        body = self.driver.find_element_by_xpath('//body')
        self.assertFalse('I am some other page content' in body.text)
        self.driver.find_elements_by_link_text('i am a link')[0].click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('I am some other page content' in body.text)

    @parallelWd.multiply
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

