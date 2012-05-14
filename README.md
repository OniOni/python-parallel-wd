# python-parallel-wd -- Run selenium test in multiple browsers easily - Python flavor

## Install

## Authors

  - Mathieu Sabourin ([OniOni](http://github.com/OniOni))  

## License

  * License - Apache 2: http://www.apache.org/licenses/LICENSE-2.0

## Usage
...

## Writing a test!

Start by importing the module 

<pre>
import wd.parallel
</pre>

<pre>
class Selenium2OnSauce(unittest.TestCase):
    def setUp(self):
        self.drivers = wd.parallel.Remote()
        self.drivers.load_config_file(os.path.join(PATH("config.json")))

    @wd.parallel.multiply
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

    @wd.parallel.multiply
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
</pre>

## Supported Methods

## More docs!
<pre>
WD is simply implementing the Selenium JsonWireProtocol, for more details see the official docs:
 - <a href="http://code.google.com/p/selenium/wiki/JsonWireProtocol">http://code.google.com/p/selenium/wiki/JsonWireProtocol</a>
</pre>

## Run the tests!
<pre>
  - Run the selenium server with chromedriver: 
      java -jar selenium-server-standalone-2.21.0.jar -Dwebdriver.chrome.driver=&lt;PATH&gt;/chromedriver
  - cd wd
  - npm install .
  - make test
  - look at the results!
</pre>
