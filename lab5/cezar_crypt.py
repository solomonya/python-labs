"""
Зашифруйте данный текстовый файл шифром Цезаря,
при этом символы первой строки файла должны циклически сдвигаться на 1,
второй строки — на 2, третьей строки — на три и т.д.
В этой задаче удобно считывать файл построчно, шифруя каждую строку в отдельности.

hello
hello
hello
hello
hello

ifmmp
jgnnq
khoor
lipps
"""


def ceasar_encode(letter, shift):
    result = ''
    for letter in line:
        if letter.isalpha():
            number = ord(letter) + shift % 32
            if number > 1103:
                number -= 32
            result += chr(number)
        else:
            result += letter
    return result


text_stream = open('crypt.txt', 'r')
text = text_stream.read().split()

print('Зашифрованные строки текста: ')
for shift, line in enumerate(text, 1):
    print(ceasar_encode(line, shift))

text_stream.close()

