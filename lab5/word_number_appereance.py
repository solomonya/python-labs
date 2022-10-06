"""
Во входном файле (вы можете читать данные из файла input.txt) записан текст.
Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов или символами конца строки.
Для каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

"""

import re
from collections import Counter


word_number_appearance = Counter(re.split(r'\s', open('appereance_number.txt', 'r').read()))

word_number_appearance_array = []

for word in word_number_appearance:
    word_number_appearance_array.append(word_number_appearance[word])

print(word_number_appearance)
print(word_number_appearance_array)
