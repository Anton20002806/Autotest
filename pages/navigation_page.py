import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v123 import browser

from .base_page import BasePage


class NavigationPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//*[@id=\"field-5\"]")
    PASSWORD_INPUT = (By.XPATH, '//*[@id=\"field-6\"]')
    BASKET_BUTTON = (By.XPATH, '//*[@class=\"menu__item\"]')
    BASKET_PAGE = (By.XPATH, '//*[@class=\"row row--plain\"]/h1')

    def navigation(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(*self.BASKET_BUTTON).click()
