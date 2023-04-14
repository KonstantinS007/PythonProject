from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
# инициализируем драйвер браузера
s = Service("chromedriver.exe")
driver = webdriver.Chrome(service=s)

# загружаем страницу
driver.get("https://b2c.passport.rt.ru/")
time.sleep(5)

element = driver.find_element(By.ID, "kc-register")
element.click()
time.sleep(5)

# находим элемент по его идентификатору
element = driver.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask")
driver.execute_script("arguments[0].style.display = 'block';", element)
element = driver.find_element(By.CSS_SELECTOR, "#page-right > div > div > div > form > div.rt-select.rt-select--search.register-form__dropdown > div > div > span.rt-input__mask > span.rt-input__mask-start")
# получаем текст элемента
text = element.text

# выводим текст элемента
print(f'{text}')

# закрываем браузер
driver.quit()
