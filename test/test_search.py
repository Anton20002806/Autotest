import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

def test_search_positive(driver):
    search_page = SearchPage(driver)
    search_page.open("https://arnypraht.com/login/")
    tovar = "Рюкзак"
    search_page.search("impofod358@1secmail.ru", "secret_sauce", tovar)
    time.sleep(10)
    email_link = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//*[@class=\"search-form__info\"]/span"))
    )
    assert email_link.text == "По запросу " + tovar, f"Failed"