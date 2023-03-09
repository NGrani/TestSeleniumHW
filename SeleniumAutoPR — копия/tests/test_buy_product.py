import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.Cart_page import Cart_page
from pages.Client_information_page import Client_information_page
from pages.Finish_page import Finish_page
from pages.Login_page import Login_page
from pages.Main_page import Main_page
from pages.Payment_page import Payment_page

@pytest.mark.run(order=2)
def test_buy_product_1(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/nagrani/Documents/Tools/Драйвера для Selenium/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test 1")

    login = Login_page(driver)
    login.autorization()

    mb = Main_page(driver)
    mb.select_product1_method()

    checkout = Cart_page(driver)
    checkout.checkout_button_method()

    cip = Client_information_page(driver)
    cip.fill_up_info()

    payment = Payment_page(driver)
    payment.click_payment_button()

    finish = Finish_page(driver)
    finish.get_screenshot_method()

    print("Finish test 1")

    time.sleep(3)
    driver.close()

@pytest.mark.run(order=3)
def test_buy_product_2(set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/nagrani/Documents/Tools/Драйвера для Selenium/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test 2")

    login = Login_page(driver)
    login.autorization()

    mb = Main_page(driver)
    mb.select_product2_method()

    checkout = Cart_page(driver)
    checkout.checkout_button_method()

    cip = Client_information_page(driver)
    cip.fill_up_info()

    payment = Payment_page(driver)
    payment.click_payment_button()

    finish = Finish_page(driver)
    finish.get_screenshot_method()

    print("Finish test 2")

    time.sleep(3)
    driver.close()

@pytest.mark.run(order=1)
def test_buy_product_3(set_up):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/nagrani/Documents/Tools/Драйвера для Selenium/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    print("Start test 3")

    login = Login_page(driver)
    login.autorization()

    mb = Main_page(driver)
    mb.select_product3_method()

    checkout = Cart_page(driver)
    checkout.checkout_button_method()

    cip = Client_information_page(driver)
    cip.fill_up_info()

    payment = Payment_page(driver)
    payment.click_payment_button()

    finish = Finish_page(driver)
    finish.get_screenshot_method()

    print("Finish test 3")

    time.sleep(3)
    driver.close()