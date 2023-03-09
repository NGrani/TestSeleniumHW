import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from pages.Coffee_machine_page import Coffee_machine_page

""" Проверяем цену товара и переходим к оформлению заказа"""
class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  """Locators"""

    checkout_button = '//a[@data-ng-href="checkout"]'
    full_price = '//span[@class="cart-full-result-price"]'
    name_product = '//a[@class="cart-full-name-link"]'
    delete_button = '//a[@data-ng-click="cartFull.clear()"]'


    # "Getters"

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    def get_full_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_price)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    def get_delete_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delete_button)))

    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print('Click checkout_button')
# """ Предусматриваем метод удаления товара из корзины"""

    def click_delete_button(self):
        self.get_delete_button().click()
        print('Click delete_button')

     # metods

    def checkout(self):
        self.get_current_url()
        coffee = Coffee_machine_page(self.driver)
        print(coffee.check_price)
        self.assert_word(self.get_full_price(), self.check_price) #проверяем цену сопоставляя с изначальной
        self.assert_word(self.get_name_product(), self.check_name)
        self.driver.execute_script('window.scrollTo(0, 60)')
        time.sleep(3)
        self.click_checkout_button()




