"""Файл с основными методами"""

from pages.base_page import BasePage

main_url = 'https://demoqa.com/text-box'


class MainPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def click(self):
        self.browser.click()

    def find(self, locator):
        return self.browser.find_element(*locator)

    def send_keys(self, keys):
        self.browser.send_keys(keys)

    def get_text(self, locator):
        self.browser.find(*locator).getText()

    @staticmethod
    def cut_start_string(string):
        return string[string.find(":") + 1:]

    @staticmethod
    def cut_end_string(string):
        return string[:string.find(":")]

    def save_screenshot(self, file_name: str):
        return self.browser.save_screenshot(f"screenshots/{file_name}.png")