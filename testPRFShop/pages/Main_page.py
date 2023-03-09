
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
"""На главной странице выбираем интересующий нас бренд товаров"""
class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


      #  """Locators"""

    delondhi_link = '/html/body/div[4]/main/div/div[2]/div[1]/nav/div/div[2]/div[2]/a/span'
    main_word = '//div[@class="catalog-title page-title"]' # для проверки попаданияя на нужную страницу

    # "Getters"

    def get_delondhi_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delondhi_link)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def click_delondhi_link(self):
        self.get_delondhi_link().click()
        print('click delondhi_link')

     # methods

    def open_brand_delonghi(self):
        self.get_current_url()
        self.click_delondhi_link()
        print(self.get_main_word().text)
        self.assert_word(self.get_main_word(), 'De`Longhi')





