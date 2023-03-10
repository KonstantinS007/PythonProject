#!/usr/bin/python3
# -*- encoding=utf8 -*-

# You can find very simple example of the usage Selenium with PyTest in this file.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     python3 -m pytest -v --driver Chrome --driver-path ~/chrome tests/*
#   Remote:
#  export SELENIUM_HOST=<moon host>
#  export SELENIUM_PORT=4444
#  pytest -v --driver Remote --capability browserName chrome tests/*
#  python -m pytest -v --driver Chrome --driver-path chromedriver.exe test_selenium_petfriends_pytest_cookie.py tests

#import time, pickle
import pytest
from Task_27.pages.petfriends import MainPage
from Task_27.pages.elements import ManyWebElements
from selenium.webdriver.common.action_chains import ActionChains

def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """

    page = MainPage(web_browser)

    # Scroll down till the end using actionchains and click on the last image
    page.scroll_down()
    page._web_driver.implicitly_wait(10)
    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')

