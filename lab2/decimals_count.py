"""
Дано двузначное число. Найдите число десятков в нем.

Входные данные
Вводится единственное число (гарантируется, что оно соответствует условию задачи).

Выходные данные
Выведите ответ на задачу.
"""
import math


def main():
    number = 0;
    print('Введите двухзначное число: ')
    number = int(input())
    decimals_count = number // 10
    print(f'Количество десятков в числе {number} равно {decimals_count}')


main()
