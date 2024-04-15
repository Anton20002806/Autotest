import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v123 import browser

from .base_page import BasePage


class BasketPage(BasePage):
    EMAIL_INPUT = (By.XPATH, "//*[@id=\"field-5\"]")
    PASSWORD_INPUT = (By.XPATH, '//*[@id=\"field-6\"]')
    BASKET_BUTTON = (By.XPATH, '//*[@class=\"menu__item\"]')
    SRC_BUTTON = (By.XPATH, '//*[@class=\"header__main\"]/nav/button')
    FILTER_BUTTON = (By.XPATH, '//*[@class=\"navbar__level\"]/div/ul/li')
    CLEAR_BUTTON = (By.XPATH, '//*[@class=\"gap\"]/form/button')
    FILTER_BUTTON3 = (By.XPATH, "//*[@class=\"cards cards--grid cards--grid-full\"]/div/div[2]/div/form/div/button")
    BASKET_BUTTON2 = (By.XPATH, '//*[@class=\"header__main\"]/div/ul/li[4]')

    def basket(self, email, password):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(Keys.ENTER)
        time.sleep(3)
        # self.driver.find_element(*self.BASKET_BUTTON2).click()
        self.driver.find_element(*self.SRC_BUTTON).click()

        time.sleep(1)
        self.driver.find_element(*self.FILTER_BUTTON).click()
        self.driver.find_element(*self.FILTER_BUTTON3).click()
        self.driver.find_element(*self.BASKET_BUTTON2).click()

