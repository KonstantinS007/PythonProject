from Task_26.pages.auth_page import AuthPage
import time
import pickle

# python -m pytest -v --driver Chrome --driver-path Task_26/chromedriver.exe


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("uzerovalex9@gmail.com")
    page.enter_pass("qwerty123")
    page.btn_click()

    #знак != или == будет зависеть от того, верные или неверные данные мы вводим
    assert page.get_relative_link() == '/all_pets', "login error"
    with open('my_cookies.txt', 'wb') as cookies:
         pickle.dump(page._web_driver.get_cookies(), cookies)
