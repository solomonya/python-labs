from copy import deepcopy
import random

def get_array_max(list):
    max = 0
    for elem in list:
        if max < elem:
            max = elem
    return max

def get_pairs_imperative(list):
    copy_list = deepcopy(list)
    first_max = get_array_max(copy_list)
    copy_list.remove(first_max)
    second_max = get_array_max(copy_list)
    return first_max * second_max

def get_pairs_sort(list):
    sorted_list = deepcopy(list)
    sorted_list.sort()
    return sorted_list[-1] * sorted_list[-2]

size = 1000000
list = []
for i in range(size):
    list.append(random.randint(0, 100))



print(get_pairs_imperative(list))
print(get_pairs_sort(list))