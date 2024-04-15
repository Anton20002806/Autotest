import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage


def test_registration_positive(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://arnypraht.com/register/")
    rand = round(random.uniform(1, 10000))
    emai = "impods" + str(rand) + "@ijio.ru"
    number = "+798656" + str(rand)
    registration_page.register(emai, "secret_sauce", "female", number)
    WebDriverWait(driver, 10).until(EC.url_to_be("https://arnypraht.com/register/"))
    success_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"h4 h--subtitled\"]"))
    )
    success_message_text = success_message_element.text
    assert "Спасибо за регистрацию!" in success_message_text, "Регистрация была успешной"
