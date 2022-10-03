"""
Даны два натуральных числа a и b.
Найдите их наибольший общий делитель d и два таких целых числа x и y, что ax+by=d.
Программа должна вывести числа d, x, y.
"""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


print(extended_gcd(26, 44))