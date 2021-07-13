def selectionSort(data):
    for stand in range(len(data) - 1):
        lowest = stand

        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index


        data[stand], data[lowest] = data[lowest], data[stand]

    return data

import random

data_list = random.sample(range(100), 50)
print(data_list)
print(selectionSort(data_list))
