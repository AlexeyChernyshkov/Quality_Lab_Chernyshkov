"""Файл для генерации случайных строк"""

import random
import string


def rand_str_generator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def random_str(length):
    return rand_str_generator(length)


def random_email(main, sld, tld):   # sld — second lvl domen, tld — top lvl domen
    return rand_str_generator(int(main)) + "@" + rand_str_generator(int(sld)) + "." + rand_str_generator(int(tld))



