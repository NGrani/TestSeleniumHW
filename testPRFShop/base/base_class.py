import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class Base():

    # constant так какмы проверяем покупку определенного товара у определенного юзера,
    # мы можем сохранить сновную информацию в константы и при необхдимости поменять их только тут.
    # Это делает наш код универсальным

    email = 'testaut@inbox.ru'
    password = 'Qwerty6543!'
    check_price = '1 030 руб.'
    check_name = 'Крышка контейнера для кофейных зёрен к кофемашине'


    def __init__(self, driver):
        self.driver = driver


    # Method get current url

    def get_current_url(self):
       current_url = self.driver.current_url
       print('Current url: ' + current_url)

    # Method assert word

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    # Method assert url

    def assert_url(self, result):
        get_url = self.driver.current_url
        print(get_url)
        assert get_url == result
        print('Good value url')

    # Method screenshot

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S')
        self.driver.save_screenshot(f'./screen/screenshot {now_date}.png')
        print('Screen saved')

    # method Move to
    def move_to_el(self, path):
        action = ActionChains(self.driver)
        elenent = self.driver.find_element(By.XPATH, path)
        action.move_to_element(elenent).perform()

