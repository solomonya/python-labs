print('Введите первое число')
first_value = float(input())
print('Введите второе число')
second_value = float(input())

first_value = 0 if first_value <= second_value else first_value
print(f'Первое число: {first_value}, Второе число: {second_value}')
