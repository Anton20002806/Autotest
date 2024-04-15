import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.navigation_page import NavigationPage

def test_navigation_positive(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.open("https://arnypraht.com/login/")
    navigation_page.navigation("impofod358@1secmail.ru", "secret_sauce")
    time.sleep(5)
    expected_url = "https://arnypraht.com/cart/"
    actual_url = navigation_page.get_current_url()
    assert actual_url == expected_url, f"Выполнено"