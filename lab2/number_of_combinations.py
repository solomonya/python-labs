def get_factorial(number):
    factorial = 1
    index = 1
    while index <= number:
        factorial *= index
        index += 1
    return factorial


def get_number_of_combinations(n, k):
    return int(get_factorial(n) / (get_factorial(k) * get_factorial(n - k)))


def main():
    print('Введите число n:')
    n = int(input())
    print('Введите число k:')
    k = int(input())
    number_of_combinations = get_number_of_combinations(n, k)
    print(f'Число сочетаний равно: {number_of_combinations}')


main()
