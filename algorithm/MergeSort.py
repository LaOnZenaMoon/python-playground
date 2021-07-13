def split(data):
    medium = int(len(data) / 2)
    left = data[:medium]
    right = data[medium:]
    print(left, right)


def merge(left_data, right_data):
    left_cursor = 0
    right_cursor = 0

    mergedList = list()

    # Case1: left/right 데이터가 아직 남아있을때
    while left_cursor < len(left_data) and right_cursor < len(right_data):
        if left_data[left_cursor] < right_data[right_cursor]:
            mergedList.append(left_data[left_cursor])
            left_cursor += 1
        else:
            mergedList.append(right_data[right_cursor])
            right_cursor += 1

    # Case2: left 데이터만 남아있을때
    while left_cursor < len(left_data):
        mergedList.append(left_data[left_cursor])
        left_cursor += 1

    # Case3: right 데이터만 남아있을때
    while right_cursor < len(right_data):
        mergedList.append(right_data[right_cursor])
        right_cursor += 1

    return mergedList


def mergeAndSplit(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)
    left = mergeAndSplit(data[:medium])
    right = mergeAndSplit(data[medium:])
    return merge(left, right)


import random

data_list = random.sample(range(100), 10)
print("before")
print(data_list)
print("after")
print(mergeAndSplit(data_list))
