import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.open("https://arnypraht.com/login/")
    login_page.login("impofod358@1secmail.ru", "secret_sauce")
    time.sleep(5)
    expected_url = "https://arnypraht.com/account/overview/"
    actual_url = login_page.get_current_url()
    assert actual_url == expected_url, f"Провалено"