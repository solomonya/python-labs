def calculate_final_temperature(temp_first, temp_second, volume_first, volume_second):
    volume_sum = volume_first + volume_second
    final_temperature = (volume_first * temp_first + volume_second * temp_second) / volume_sum
    return {'temperature': round(final_temperature), 'volume': volume_sum}


print('Введите температуру Т1...')
first_temp = int(input())
print('Введите температуру T2')
second_temp = int(input())
print('Введите объём V1')
first_vol = int(input())
print('Введите объём V2')
second_vol = int(input())
result = calculate_final_temperature(first_temp, second_temp, first_vol, second_vol)
print(f'Температура: {result["temperature"]}, Объём: {result["volume"]}')

