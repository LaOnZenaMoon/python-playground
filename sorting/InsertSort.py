import random


class InsertSort:

    def perform(self, target):
        if len(target) <= 1:
            return target

        for index in range(1, len(target)):
            temp = target[index]
            cursor = index - 1

            # ">": desc, "<": asc
            while (cursor >= 0) and (target[cursor] > temp):
                target[cursor + 1] = target[cursor]
                cursor -= 1

            target[cursor + 1] = temp

        return target

insertSort = InsertSort()
randomlist = []
for index in range(0, 10):
    randomlist.append(random.randrange(0, 100))
print(randomlist)

sortedList = insertSort.perform(randomlist)
print(sortedList)