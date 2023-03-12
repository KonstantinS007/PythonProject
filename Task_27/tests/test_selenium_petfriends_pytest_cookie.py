#!/usr/bin/python3
# -*- encoding=utf8 -*-
from selenium.webdriver.common.by import By
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
#  python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests


import time
from Task_27.pages.petfriends import MainPage


def test_petfriends(web_browser):
    """ Authorize to Petfriends via cookies and create a screenshot when loginpage is successfull. """

    page = MainPage(web_browser)

    # Scroll down till the end using actionchains and click on the last image
    # page.scroll_down()
    page._web_driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')


def test_popen_page(web_browser):
    """ This is advanced function which also checks that all images completely loaded. """

    MainPage(web_browser)

    page_loaded = False
    images_loaded = False

    script = ("return arguments[0].complete && typeof arguments[0].natural"
              "Width != \"undefined\" && arguments[0].naturalWidth > 0")

    # Wait until page loaded (and scroll it, to make sure all objects will be loaded):
    while not page_loaded and not images_loaded:
        time.sleep(1)

        # Scroll down and wait when page will be loaded:
        web_browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        page_loaded = web_browser.execute_script("return document.readyState == 'complete';")

        # Make sure that every image loaded completely
        # (sometimes we have to scroll to the image to push browser upload it):
        pictures = web_browser.find_elements(By.XPATH, "//img")
        res = []

        for image in pictures:
            src = image.get_attribute('src')
            if src:
                # Scroll down to each image on the page:
                image.location_once_scrolled_into_view
                web_browser.execute_script("window.scrollTo(0, 155)")

                image_ready = web_browser.execute_script(script, image)

                if not image_ready:
                    # if the image not ready, give it a try to load and check again:
                    time.sleep(5)
                    image_ready = web_browser.execute_script(script, image)

                res.append(image_ready)

        # Check that every image loaded and has some width > 0:
        images_loaded = False not in res

    # Go up:
    web_browser.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
