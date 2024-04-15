import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.basket_page import BasketPage

def test_search_positive(driver):
    basket_page = BasketPage(driver)
    basket_page.open("https://arnypraht.com/login/")
    basket_page.basket("impofod358@1secmail.ru", "secret_sauce")
    time.sleep(5)
    email_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"pos\"]/div[2]"))
    )
    assert 0 <= int(email_link.text), f"Failed + " + email_link