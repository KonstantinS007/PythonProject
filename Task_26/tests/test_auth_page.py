from ..pages.auth_page import AuthPage
import time
import pickle

# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests/test_auth_page.py


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("uzerovalex9@gmail.com")
    page.enter_pass("qwerty123")
    page.btn_click()

    #
    assert page.get_relative_link() == '/all_pets', "login error"

