import random


class SelectSort:

    def perform(self, target):
        if len(target) <= 1:
            return target

        for index1 in range(len(target)-1):
            indexMinimum = index1

            for index2 in range(index1+1, len(target)):
                if(target[index2] < target[indexMinimum]):
                    indexMinimum = index2

            temp = target[indexMinimum]
            target[indexMinimum] = target[index1]
            target[index1] = temp

        return target

selectSort = SelectSort()
randomlist = []
for index in range(0, 10):
    randomlist.append(random.randrange(0, 100))
print(randomlist)

sortedList = selectSort.perform(randomlist)
print(sortedList)