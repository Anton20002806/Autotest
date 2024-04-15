from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from .base_page import BasePage


class RegistrationPage(BasePage):
    GENDER_MALE_RADIO = (By.XPATH, '//*[@class=\"fieldset__field field-row choice\"]/label[1]')
    GENDER_FEMALE_RADIO = (By.XPATH, '//*[@class=\"fieldset__field field-row choice\"]/label[2]')

    EMAIL_INPUT = (By.XPATH,"//*[@id=\"office-auth-register-email\"]")
    MOBILE_INPUT = (By.XPATH,'//*[@id=\"office-auth-register-mobilephone\"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@id=\"office-register-form-password\"]')
    INPUT_DAY = (By.XPATH, "//*[@class=\"select2-selection select2-selection--single select date-select__day\"]")
    INPUT_MOUNT = (By.XPATH, '//*[@class=\"select2-selection select2-selection--single select date-select__month\"]')
    INPUT_YEAR = (By.XPATH, '//*[@class=\"select2-selection select2-selection--single select date-select__year\"]')
    POLICE_BUTTON = (By.XPATH, '//*[@class=\"checkbox checkbox--basic checkbox--s checkbox--policy\"]/span[1]')
    INPUT_DAY_B = (By.XPATH, "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span[2]/ul/li")
    INPUT_MOUNT_B = (By.XPATH, "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span[2]/ul/li")
    INPUT_YEAR_B = (By.XPATH, "//*[@class=\"select2-container select2-container--default select2-container--open\"]/span/span[2]/ul/li[25]")
    def select_gender(self, gender):
        if gender == "male":
            self.driver.find_element(*self.GENDER_MALE_RADIO).click()
        elif gender == "female":
            self.driver.find_element(*self.GENDER_FEMALE_RADIO).click()
        else:
            raise ValueError("Должен быть 'male' или 'female'")

    def register(self, email, password, gender, mobile):
        self.select_gender(gender)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.MOBILE_INPUT).send_keys(mobile)

        # self.driver.find_element(*self.POLICE_BUTTON).click()
        self.driver.find_element(*self.INPUT_DAY).click()
        self.driver.find_element(*self.INPUT_DAY_B).click()
        self.driver.find_element(*self.INPUT_MOUNT).click()
        self.driver.find_element(*self.INPUT_MOUNT_B).click()
        self.driver.find_element(*self.INPUT_YEAR).click()
        self.driver.find_element(*self.INPUT_YEAR_B).click()
        self.driver.find_element(*self.POLICE_BUTTON).click()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(Keys.ENTER)

