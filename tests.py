import unittest
import time

class NewUpdate(unittest.TestCase):  

    def test_to_update_CV(self):  
        # open home page
        self.browser.get('http://localhost:8000')

        # change to cv page


        # page title and header
        self.assertIn('To-Do', self.browser.title)  
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # start to edit
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')