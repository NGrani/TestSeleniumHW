import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
"""Заполняем данные клиента"""
class Info_client_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  """Locators"""

    e_mail_loc =     '/html/body/div[4]/main/div/div[2]/div[4]/div[1]/article/div[2]/div/form/div/div[1]/span[2]/span'
    first_name = '//input[@id="Data_User_FirstName"]'
    last_name = '//input[@data-ng-model="checkout.newCustomer.lastname"]'
    number_phone = '//input[@id="Data_User_Phone"]'
    counrty = '//input[@id="Data_Contact_Country"]'
    region = '//input[@id="Data_Contact_Region"]'
    city = '//input[@id="Data_Contact_City"]'
    order_comment = '//textarea[@id="CustomerComment"]'
    cart = '//a[@class="cs-l-2 cs-bg-9 cart-mini-main-link icon-bag-before"]'
    go_to_cart_button = '//a[@class="btn btn-buy btn-xsmall cart-mini-btn-cart"]'

    # "Getters"

    def get_e_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail_loc)))

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_number_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_phone)))

    def get_counrty(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.counrty)))

    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_order_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_comment)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    # Actions


    def input_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        print('input_first_name')

    def input_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        print('input_last_name')

    def input_number_phone(self, number_phone):
        self.get_number_phone().clear()
        self.get_number_phone().send_keys(number_phone)
        print('input_number_phone')

    def input_counrty(self, counrty):
        self.get_counrty().clear()
        self.get_counrty().send_keys(counrty)
        print('input_counrty')

    def input_region(self, region):
        self.get_region().clear()
        self.get_region().send_keys(region)
        print('input region')

    def input_city(self, city):
        self.get_city().clear()
        self.get_city().send_keys(city)
        self.get_city().send_keys(Keys.RETURN)
        print('input city')

    def input_order_comment(self, order_comment):
        self.get_order_comment().clear()
        self.get_order_comment().send_keys(order_comment)
        print('order_comment')

    def click_cart(self):
        self.get_cart().click()
        print('Click get_cart')

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Click go_to_cart_button')


     # metods

    def fill_up_info(self):
        self.get_current_url()
        self.assert_word(self.get_e_mail(), self.email)
        self.input_first_name('Georgii')
        self.input_last_name('Markarian')
        self.input_number_phone('79992223344')
        self.input_counrty('Russia')
        self.input_region('Krasnodarskii')
        self.input_city('Sochi')
        self.get_screenshot() # делаем скриншот с заполнеными данными
        self.driver.execute_script('window.scrollTo(0, 1000)')
        self.input_order_comment('Tест завершен. Далее создается и подтверждается заказ.'
                                 ' Чтобы не создавать фальшивые заказы, я остановлюсь на этом шаге. '
                                 'Сейчас произойдет удаление товара из корзины')
        time.sleep(5)
        """Так как мы не можем создать заказ(заказ далее попадает в обраблотку), мы проводим продцедуру удаления товара из корзины"""

        self.driver.execute_script('window.scrollTo(0, 0)')
        self.click_cart()
        self.click_go_to_cart_button()




