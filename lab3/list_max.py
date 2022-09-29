"""
Дан список чисел. Выведите значение наибольшего элемента в списке, а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""

import random

def get_list_max(numbers_list):
    max = 0
    max_index = 0
    for idx, i in enumerate(numbers_list):
        if max < i:
            max = i
            max_index = idx
    return max, max_index

def main():
    list = []

    print("Введите количество элементов: ")
    elem_amount = int(input())

    for num in range(elem_amount):
        list.append(random.randint(1, 1000))

    print(list)
    print(get_list_max(list))


main()