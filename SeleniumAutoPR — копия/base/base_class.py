import datetime


class Base():

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