
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


      #  """Locators"""

    user_first_name = "//input[@id='first-name']"
    user_last_name= "//input[@id='last-name']"
    user_postcode = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"


    # "Getters"

    def get_user_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_first_name)))

    def get_user_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_last_name)))

    def get_user_postcode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_postcode)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def input_user_first_name(self, user_first_name):
        self.get_user_first_name().send_keys(user_first_name)
        print('Input first name')

    def input_user_last_name(self, user_last_name):
        self.get_user_last_name().send_keys(user_last_name)
        print('Input last name')

    def input_user_postcode(self, user_postcode):
        self.get_user_postcode().send_keys(user_postcode)
        print('Input code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Continue click')

     # metods

    def fill_up_info(self):
        self.get_current_url()
        self.input_user_first_name('Georgii')
        self.input_user_last_name('Markarian')
        self.input_user_postcode('1234')
        self.click_continue_button()


