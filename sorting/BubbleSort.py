import random


class BubbleSort:

    def perform(self, target):
        if len(target) <= 1:
            return target

        for index1 in range(1, len(target)):
            for index2 in range(0, len(target)-1):
                if(target[index2] > target[index2+1]):
                    temp = target[index2]
                    target[index2] = target[index2+1]
                    target[index2+1] = temp
                    print(target)

        return target

bubbleSort = BubbleSort()
randomlist = []
for index in range(0, 10):
    randomlist.append(random.randrange(0, 100))
print(randomlist)

sortedList = bubbleSort.perform(randomlist)
print(sortedList)