
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Payment_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


      #  """Locators"""

    payment_button = "//button[@id='finish']"

    # "Getters"

    def get_payment_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_button)))



    # Actions

    def click_payment_button(self):
        self.get_payment_button().click()
        print('Click checkout_button')


     # metods

    def checkout_button_method(self):
        self.get_current_url()
        self.click_payment_button()





