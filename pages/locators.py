"""Файл с локаторами"""

from selenium.webdriver.common.by import By


class Labels:
    label_name = (By.ID, 'userName-label')
    label_email = (By.ID, 'userEmail-label')
    label_current_address = (By.ID, 'currentAddress-label')
    label_permanent_address = (By.ID, 'permanentAddress-label')


class Input:
    #   Класс с локаторами для полей ввода
    input_name = (By.CSS_SELECTOR, '#userForm #userName')
    input_email = (By.CSS_SELECTOR, '#userForm #userEmail')
    input_current_address = (By.CSS_SELECTOR, '#userForm #currentAddress')
    input_permanent_address = (By.CSS_SELECTOR, '#userForm #permanentAddress')
    submit_btn = (By.ID, 'submit')


class Output:
    # Класс с локаторами для поля вывода
    output_name = (By.CSS_SELECTOR, '#output #name')
    output_email = (By.CSS_SELECTOR, '#output #email')
    output_current_address = (By.CSS_SELECTOR, '#output #currentAddress')
    output_permanent_address = (By.CSS_SELECTOR, '#output #permanentAddress')

