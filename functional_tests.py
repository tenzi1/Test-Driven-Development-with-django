# group of tests for Functional Testing
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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

    #helper method
    def check_for_row_in_list_table(self, row_text):
        table = self.driver.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #user visits homepage
        self.driver.get('http://localhost:8000/')
        #user gets homepage with title 'To-Do' in it
        self.assertIn('To-Do', self.driver.title)
        #user notices header mention to-do lists.
        header_text = self.driver.find_element(By.TAG_NAME, "h1").text
        self.assertIn('To-Do', header_text)
        
        #user is invited to enter a to-do iteme 
        inputbox = self.driver.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
        )
        
        #user types "Clean room" into a text box
        inputbox.send_keys('Clean room')

        #when user hits enter, the page updates and now the page lists 
        #"1: Clean room" as an item in to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #page updates again and shows both items on list
        self.check_for_row_in_list_table('1: Clean room')
        self.check_for_row_in_list_table('2: Cook Food')

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()

