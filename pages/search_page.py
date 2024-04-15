import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v123 import browser

from .base_page import BasePage


class SearchPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//*[@id=\"field-5\"]")
    PASSWORD_INPUT = (By.XPATH, '//*[@id=\"field-6\"]')
    BASKET_BUTTON = (By.XPATH, '//*[@class=\"menu__item\"]')
    SRC_BUTTON = (By.XPATH, '//*[@class=\"sign search-page-invisible\"]')
    SRC_INPUT = (By.XPATH, '//*[@class=\"page__pillar\"]/form/div/input')

    def search(self, email, password, tovar):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(*self.SRC_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*self.SRC_INPUT).send_keys(tovar)
        self.driver.find_element(*self.SRC_INPUT).send_keys(Keys.ENTER)
