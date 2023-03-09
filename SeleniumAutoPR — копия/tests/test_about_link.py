import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Login_page import Login_page
from pages.Main_page import Main_page



def test_about_link():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service('/Users/nagrani/Documents/Tools/Драйвера для Selenium/chromedriver_mac_arm64/chromedriver')
    driver = webdriver.Chrome(options=options, service=g)

    login = Login_page(driver)
    login.autorization()

    mb = Main_page(driver)
    mb.select_menu_about()



    time.sleep(3)
    driver.close()
