# python-parallel-wd -- Run selenium test in multiple browsers easily - Python flavor

## Install
...

## Authors

  - Mathieu Sabourin ([OniOni](http://github.com/OniOni))  

## License

  * License - Apache 2: http://www.apache.org/licenses/LICENSE-2.0

## Usage
...

## Writing a test !

Start by importing the module 

<pre>
import wd.parallel
</pre>

The test should be implemented as a unittest TestCase. So go ahead and do that 

<pre>
class Selenium2OnSauce(unittest.TestCase):
</pre>

In the set up you should create your browsers configurations. Or you could just load them from a json file.

<pre>
    def setUp(self):
        self.drivers = wd.parallel.Remote()
        self.drivers.load_config_file(os.path.join(PATH("config.json")))
</pre>

Now just write your test as you would for a unique browser. Test should be run on the self.driver attribute. Just use the @multiply decoration to run the test in all the browser you set up. Check out the <a href='#'>selenium</a> documentation for available methods.

<pre>
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

</pre>

The tear down method works just like the test cases. Just work as if there was one browser and add the @multiply decorator.

<pre>
    @wd.parallel.multiply
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
</pre>

## Supported Methods
Check out the python wd <a href='#'>implementation<a> it has all the documentation about actual tests.

## More docs!
<pre>
WD is simply implementing the Selenium JsonWireProtocol, for more details see the official docs:
 - <a href="http://code.google.com/p/selenium/wiki/JsonWireProtocol">http://code.google.com/p/selenium/wiki/JsonWireProtocol</a>
</pre>

