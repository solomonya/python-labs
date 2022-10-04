"""
Дан квадратный массив. Поменяйте местами элементы, стоящие на главной и побочной диагонали,
при этом каждый элемент должен остаться в том же столбце
(то есть в каждом столбце нужно поменять местами элемент на главной диагонали и на побочной диагонали).
Решение оформите в виде функции SwapDiagonals (A).
"""


def swap(a):
    n = len(a)
    for i in range(n):
        a[i][i], a[n-i-1][i] = a[n-i-1][i], a[i][i]


def show(a):
    for r in a:
        print (', '.join(['{:2d}'.format(i) for i in r]))

print('Введите размерность матрицы: ')
matrix_size = int(input())

a = [[j + i * matrix_size + 1 for j in range(matrix_size)] for i in range(matrix_size)]

show(a)
swap(a)
print()
show(a)
