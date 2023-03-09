from Task_26.pages.auth_page import AuthPage
import time

# python -m pytest -v --driver Chrome --driver-path Task_26/chromedriver.exe


def test_auth_page(selenium):
    page = AuthPage(selenium)
    page.enter_email("uzerovalex9@gmail.com")
    page.enter_pass("qwerty123")
    page.btn_click()

    #���� != ��� == ����� �������� �� ����, ������ ��� �������� ������ �� ������
    assert page.get_relative_link() == '/all_pets', "login error"
