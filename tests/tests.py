"""Файл с тестом"""

from pages.main_page import *
from pages.locators import *
from pages.random_string import *
import time


def test_1(browser):
    test = MainPage(browser, main_url)
    test.get()

    try:
        #   Создаем тестовые строки
        rand_name = random_str(10)
        rand_email = random_email(8, 4, 2)
        rand_current_address = random_str(30)
        rand_permanent_address = random_str(40)

        #   Заполняем инпуты
        test.find(Input.input_name).send_keys(rand_name)
        test.find(Input.input_email).send_keys(rand_email)
        test.find(Input.input_current_address).send_keys(rand_current_address)
        test.find(Input.input_permanent_address).send_keys(rand_permanent_address)
        test.find(Input.submit_btn).click()

        flag = 0    # Флаг для финальной проверки

        name_string = test.find(Labels.label_name).text + ":" + rand_name
        email_string = test.find(Labels.label_email).text + ":" + rand_email
        current_address_string = test.find(Labels.label_current_address).text + ":" + rand_current_address
        permanent_address_string = test.find(Labels.label_permanent_address).text + ":" + rand_permanent_address

        out_name_string = test.find(Output.output_name).text
        out_email_string = test.find(Output.output_email).text
        out_current_address_string = test.find(Output.output_current_address).text
        out_permanent_address_string = test.find(Output.output_permanent_address).text

        #   Проверки
        if name_string != out_name_string:
            print(f" Failed: '{name_string}' != '{out_name_string}'")
            flag = 1

        if email_string != out_email_string:
            print(f"Failed: '{email_string}' != '{out_email_string}'")
            flag = 1

        if current_address_string != out_current_address_string:
            print(f"Failed: '{current_address_string}' != '{out_current_address_string}'")
            flag = 1

        if permanent_address_string != out_permanent_address_string:
            print(f"Failed: '{permanent_address_string}' != '{out_permanent_address_string}'")
            flag = 1

        #   Финальная проверка
        assert flag == 0, "Some problems"
    finally:
        #   Сохраняем скриншот
        test.save_screenshot('file_1')

    time.sleep(2)
