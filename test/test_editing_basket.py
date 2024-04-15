import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.basket_editing_page import BasketEditionPage

def test_search_positive(driver):
    basket_editing_page = BasketEditionPage(driver)
    basket_editing_page.open("https://arnypraht.com/login/")
    basket_editing_page.basket_edition("impofod358@1secmail.ru", "secret_sauce")
    time.sleep(5)
    email_link = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"page__container\"]/div/div/div/h1"))
    )
    assert "В вашей корзине пусто" == email_link.text, f"Failed + " + email_link.text