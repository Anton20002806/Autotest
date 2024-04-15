import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.filter_page import FilterPage

def test_search_positive(driver):
    filter_page = FilterPage(driver)
    filter_page.open("https://arnypraht.com/login/")
    filter_page.filter("impofod358@1secmail.ru", "secret_sauce")
    time.sleep(5)
    email_link = WebDriverWait(driver, 10).until(
      EC.visibility_of_element_located((By.XPATH, "//*[@class=\"pos\"]/div/div[2]/div/a/div/span"))
    )
    email_link2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"cards cards--grid cards--grid-full\"]/div[15]/div[2]/div/a/div/span"))
    )
    print(email_link2.text)
    assert email_link.text <= email_link2.text, f"Failed + " + email_link