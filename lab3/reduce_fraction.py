"""
Даны два натуральных числа n и m. Сократите дробь nm, то есть выведите два других числа p и q таких,
что nm=pq и дробь pq — несократимая.Решение оформите в виде функции ReduceFraction(n, m),
получающая значения n и m и возвращающей кортеж из двух чисел.
"""


def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


def reduce_fraction(n, m):
    gcd = gcd_recursion(n, m)
    return n // gcd, m // gcd


def main():
    print("Введите числитель: ")
    numerator = int(input())
    print("Введите знаменатель")
    denumerator = int(input())
    print(reduce_fraction(numerator, denumerator))


main()
