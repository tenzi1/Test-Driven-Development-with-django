# group of tests for Functional Testing
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
 
#check out homepage
# driver.get('http://localhost:8000')

#notice page title and header mention to-do lists
# assert 'To-Do' in driver.title

#closes the browser
# driver.quit()


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title)
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

