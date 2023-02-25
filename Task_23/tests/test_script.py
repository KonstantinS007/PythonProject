import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# pytest test_script.py


class TestLoginStellarBurgers:

    def setup(self):
        self.user = "Kot@kot.ru"
        self.password = "kot987"

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def close(self):
        self.driver.quit()

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(self.user)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Войти')]").click()
        assert WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Оформить заказ')]")))

    def test_login_by_button_in_form(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Войти в аккаунт')]"))).click()
        self.login()

    def test_login_from_cabinet(self):
        self.open()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Личный Кабинет')]"))).click()
        self.login()

    def teardown(self):
        self.close()
