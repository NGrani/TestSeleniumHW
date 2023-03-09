import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

"""Авторизуемся в системе под тестовым аккаунтом"""

class Login_page(Base):

    url = 'https://prfshop.ru/login'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


      #  """Locators"""

    user_name = '//input[@autocomplete="email"]'
    user_password = '//input[@autocomplete="off"]'
    login_button = '//input[@type="submit"]'
    main_word = '//span[@class="menu-dropdown-root-text"]' # Для проверки попадания на главную страницу

    # "Getters"

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('input user name')

    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print('input user password')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click login button')


     # metods

    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.input_user_name(self.email)
        self.input_user_password(self.password)
        self.click_login_button()
        time.sleep(4)
        print(self.get_main_word().text)
        self.assert_word(self.get_main_word(), 'Все товары')





