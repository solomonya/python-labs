def get_numbers():
    numbers = []
    counter = 0
    print('Введите 3 числа:')
    while counter < 3:
        numbers.append(int(input()))
        counter += 1

    return numbers


def get_uniq_list(numbers):
    uniq_list = []
    index = 0
    while index < 3:
        if numbers[index] not in uniq_list:
            uniq_list.append(numbers[index])
        index += 1

    return uniq_list


def get_duplicates_amount(uniq_list):
    length = len(uniq_list)

    duplicates_hash = {
        1: 3,
        2: 2,
        3: 0
    }

    return duplicates_hash[length]


def main():
    numbers = get_numbers()
    uniq_list = get_uniq_list(numbers)
    duplicates_amount = get_duplicates_amount(uniq_list)
    print(f'Количество повторений в {numbers}: {duplicates_amount}')


main()
