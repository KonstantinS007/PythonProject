#!/usr/bin/python3
# -*- encoding=utf8 -*-
import pickle
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
#     python -m pytest -v --driver Chrome --driver-path Task_24/chromedriver.exe test_selenium_petfriends_pytest.py
#     python -m pytest -v --driver Chrome test_selenium_simple.py
import codecs
import time
from selenium.webdriver.common.by import By

# def test_petfriends(selenium):
#     """ Search some phrase in google and make a screenshot of the page. """
#
#     # Open PetFriends base page:
#     selenium.get("https://petfriends.skillfactory.ru")
#
#     time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!
#
#     # Find the field for search text input:
#     btn_newuser = selenium.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
#
#     btn_newuser.click()
#
#     btn_exist_acc = selenium.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
#     btn_exist_acc.click()
#
#     field_email = selenium.find_element(By.ID, "email")
#     field_email.click()
#     field_email.clear()
#     field_email.send_keys("uzerovalex9@gmail.com")
#
#     field_pass = selenium.find_element(By.ID, "pass")
#     field_pass.click()
#     field_pass.clear()
#     field_pass.send_keys("qwerty123")
#
#     btn_submit = selenium.find_element(By.XPATH, "//button[@type='submit']")
#     btn_submit.click()
#
#     # Save cookies of the browser after the login
#     with open('my_cookies.txt', 'wb') as cookies:
#         pickle.dump(selenium.get_cookies(), cookies)
#
#     # Make the screenshot of browser window:
#     if web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets':
#         # Make the screenshot of browser window:
#         selenium.save_screenshot('result_petfriends.jpg')
#     else:
#         raise Exception("login error")


def test_petfriends(web_browser):
   # Open PetFriends base page:
   web_browser.get("https://petfriends.skillfactory.ru/")

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   # click on the new user button
   btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
   btn_newuser.click()

   # click existing user button
   btn_exist_acc = web_browser.find_element(By.LINK_TEXT, u"У меня уже есть аккаунт")
   btn_exist_acc.click()

   # add email
   field_email = web_browser.find_element(By.ID, "email")
   field_email.clear()
   field_email.send_keys("uzerovalex9@gmail.com")

   # add password
   field_pass = web_browser.find_element(By.ID, "pass")
   field_pass.clear()
   field_pass.send_keys("qwerty123")

   # click submit button
   btn_submit = web_browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
   btn_submit.click()
   #  By.XPATH, "a.nav-link[href='/my_pets']"

   time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

   assert  web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets',"login error"
   with open('../my_cookies.txt', 'wb') as cookies:
      pickle.dump(web_browser.get_cookies(), cookies)
