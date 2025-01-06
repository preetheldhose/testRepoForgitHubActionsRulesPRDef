#!/usr/local/bin/python3

from selenium import webdriver
import time

# Initialize the WebDriver (using Chrome)
driver = webdriver.Chrome()

# Open a webpage
driver.get("https://www.google.com")

# Maximize the browser window
driver.maximize_window()

# Perform any actions
print("Window maximized")

# Print the page title
print(driver.title)

# Time in seconds
time.sleep(5)

# Close the browser
driver.quit()
