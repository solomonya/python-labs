"""
67. Дано натуральное число п (п <= 100).
а) Сколько цифр в числе п?
б) Чему равна сумма его цифр?
в) Найти последнюю цифру числа п.
г) Найти первую цифру числа я.
д) В предположении, что я ^ 1 0 , найти предпоследнюю
"""
import random
from functools import reduce


def get_digits_amount(number):
    return len(str(number))


def get_digits_sum(number):
    return reduce(lambda x, y: x + y, list(map(int, list(str(number)))))


def get_last_digit(number):
    return list(str(number))[-1]


def get_first_digit(number):
    return list(str(number))[0]


def get_penultimate_digit(number):
    return -1 if len(str(number)) < 2 else list(str(number))[-2]


number = random.randint(1, 100)
print(f'Число: {number}')

results = {
    "digit_amount": get_digits_amount(number),
    "digit_sum": get_digits_sum(number),
    "last_digit": get_last_digit(number),
    "first_digit": get_first_digit(number),
    "penultimate_digit": get_penultimate_digit(number)
}

print(f'В числе {results["digit_amount"]} цифры,\n'
      f'Сумма цифр: {results["digit_sum"]},\n'
      f'Последняя цифра {results["last_digit"]},\n'
      f'Первая цифра {results["first_digit"]}, \n'
      f'Предпоследняя цифра {results["penultimate_digit"]}')
