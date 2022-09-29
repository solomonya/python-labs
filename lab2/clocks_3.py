def main():
    print('Введите угол a:')
    angle = float(input())
    print(int(angle // 30), int(angle % 30 * 2), int(angle % 0.5 * 120))


main()