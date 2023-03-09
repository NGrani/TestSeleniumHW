import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
""" Фильтруем товары по цене и выбираем нужный нам товар"""
class Coffee_machine_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #  """Locators"""

    show_filter_button = '/html/body/div[4]/main/div/div[2]/div[2]/article/div/form/div[5]/input[1]'
    slider_min = '//div[@class="ngrs-handle ngrs-handle-min"]'
    slider_max = '//div[@class="ngrs-handle ngrs-handle-max"]'
    add_to_cart_button = '//a[@data-product-id="2348"]'
    go_to_cart = '//a[@class="btn btn-middle btn-buy"]'
    price_product = '//span[@data-ng-bind-html="cartPopup.item.Price"]'
    name_product = '//a[@class="cart-popup-product-link"]'

    # "Getters"

    def get_show_filter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_filter_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_name_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_product)))

    # Actions

    def set_up_slider(self, xpath, count):
        action = ActionChains(self.driver)
        slider = self.driver.find_element(By.XPATH, xpath)
        action.click_and_hold(slider).move_by_offset(count, 0).release().perform()
        print('Slider set up')

    def click_show_filter_button(self):
        self.get_show_filter_button().click()
        print('Click show_filter_button')

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click add_to_cart_button')

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print('Сlick_go_to_cart')


     # metods

    def select_item(self):
        self.get_current_url()
        self.driver.execute_script('window.scrollTo(0, 600)')
        self.set_up_slider(self.slider_max, -100)
        self.set_up_slider(self.slider_min, 30)
        self.click_show_filter_button()
        self.get_screenshot() # делаем скриншот успешной фильтрации
        self.click_add_to_cart_button()
        self.assert_word(self.get_price_product(), self.check_price)
        self.assert_word(self.get_name_product(), self.check_name)
        time.sleep(3)
        self.click_go_to_cart()




