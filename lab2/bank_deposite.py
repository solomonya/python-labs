def get_minimum_period(deposite_amount, annual_rate, amount_accumulated):
    updated_deposite_amount = deposite_amount
    years = 0

    if updated_deposite_amount >= amount_accumulated:
        return 0

    while(updated_deposite_amount < amount_accumulated):
        updated_deposite_amount += int(updated_deposite_amount * (annual_rate / 100))
        years += 1

    return years


def main():
    print('Введите сумму вклада:')
    deposite_amount = int(input())
    print('Введите годовую ставку:')
    annual_rate = float(input())
    print('Введите желаемую сумму накопления')
    amount_accumulated = int(input())

    minimum_period = get_minimum_period(deposite_amount, annual_rate, amount_accumulated)
    print(f'Количество лет, через которое накопится желаемая сумма равна: {minimum_period} годам')


main()