"""Файл с основным методом для открытия браузера"""


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get(self):
        self.browser.get(self.url)

