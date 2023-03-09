
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
"""На странице бренда выбираем нужную категорию"""
class Delonghi_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


      #  """Locators"""

    coffee_machine = '/html/body/div[4]/main/div/div[2]/div[3]/div[4]/div[4]/div/div/div/a'
    main_word = '//div[@class="catalog-title page-title"]'

    # "Getters"

    def get_coffee_machine(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.coffee_machine)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_coffee_machine(self):
        self.get_coffee_machine().click()
        print('click delondhi_link')


     # metods

    def open_coffee_machine(self):
        self.get_current_url()
        self.click_coffee_machine()
        self.assert_url('https://prfshop.ru/delonghi/kofevarki-i-kofemashiny-delonghi') #проверяем, что мы попали на нужную страницу





