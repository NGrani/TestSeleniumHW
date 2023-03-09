import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Coffee_machine_page import Coffee_machine_page
from pages.Delonghi_page import Delonghi_page
from pages.Login_page import Login_page
from pages.Main_page import Main_page
from pages.cart_page import Cart_page
from pages.info_client_page import Info_client_page


# @pytest.mark.run(order=2)
def test_buy_product_1():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/nagrani/Documents/QAtests/testPRFShop/utilites/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test 1")

    login = Login_page(driver)
    login.autorization()

    main = Main_page(driver)
    main.open_brand_delonghi()

    delonghi = Delonghi_page(driver)
    delonghi.open_coffee_machine()

    coffee = Coffee_machine_page(driver)
    coffee.select_item()

    cart = Cart_page(driver)
    cart.checkout()

    fill_up = Info_client_page(driver)
    fill_up.fill_up_info()

    cart.click_delete_button()


    print("Finish test 1")

    time.sleep(3)
    driver.close()
