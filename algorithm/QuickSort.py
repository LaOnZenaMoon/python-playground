def quickSort1(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return quickSort1(left) + [pivot] + quickSort1(right)


def quickSort2(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left, right = list(), list()

    # list comprehension
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot <= item]

    return quickSort2(left) + [pivot] + quickSort2(right)


import random

data_list = random.sample(range(100), 10)
print("before")
print(data_list)
print("after")
print(quickSort1(data_list))
print(quickSort2(data_list))
