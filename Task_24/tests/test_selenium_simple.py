#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#python -m pytest -v --driver Chrome --driver-path Task_24/chromedriver.exe  test_selenium_simple.py
#  pytest -v --driver Chrome --driver-path pages/chromedriver.exe tests/test_auth_page.py > myoutput.txt
#python -m pytest -v --driver Chrome --driver-path chromdriver.exe tests/test_selenium_simple.py
#   python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_selenium_simple.py > myoutput.txt
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """
    # selenium = webdriver.Chrome(executable_path=r"/Users/User/PycharmProjects/PythonProject/drivers/Chrome/chromedriver.exe")
    # Open google search page:
    selenium.get('https://google.com')

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Find the field for search text input:
    search_input = selenium.find_element(By.NAME, 'q')

    # Enter the text for search:
    search_input.clear()
    search_input.send_keys('Selenium 4')

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search:
    search_button = selenium.find_element(By.NAME, 'btnK')
    search_button.submit()
    #search_button.click()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window:
    selenium.save_screenshot('result.png')

