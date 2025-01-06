#!/usr/local/bin/python3

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

        # Maximize the browser window
        self.driver.maximize_window()

        # Perform any actions
        print("Window maximized")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)

        titleString = driver.title;
        print("Printing titleString : ", titleString)

        # Time in seconds
        time.sleep(3)

        elem = driver.find_element(By.NAME, "q")

        # Time in seconds
        time.sleep(3)

        elem.send_keys("python")

        # Time in seconds
        time.sleep(3)

        elem.send_keys(Keys.RETURN)

        # Time in seconds
        time.sleep(3)

        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
