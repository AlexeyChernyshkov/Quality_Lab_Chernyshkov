"""Файл с фикстурой конфигурациями браузера"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()


chrome_options = Options()
chrome_options.page_load_strategy = 'eager' # Запуск страницы в режиме "жаждящий", так как при открытии долго прогружается страница
chrome_options.add_argument('log-level=3')  # Убираем лишние логи про сертификат в терминале






