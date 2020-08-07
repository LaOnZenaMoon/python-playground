import random


class MergeSort:

    def perform(self, target):
        if len(target) == 1:
            return target

        # Decomposition
        targetToSort1 = []
        targetToSort2 = []
        for index in range(len(target)):
            if(len(target) / 2 > index):
                targetToSort1.append(target[index])
            else:
                targetToSort2.append(target[index])

        # Recursion
        targetToSort1 = self.perform(targetToSort1)
        targetToSort2 = self.perform(targetToSort2)

        # Aggregation
        indexCount1 = 0
        indexCount2 = 0
        for index in range(len(target)):
            if indexCount1 == len(targetToSort1):
                target[index] = targetToSort2[indexCount2]
                indexCount2 += 1
            elif indexCount2 == len(targetToSort2):
                target[index] == targetToSort1[indexCount1]
            elif targetToSort1[indexCount1] > targetToSort2[indexCount2]:
                target[index] = targetToSort2[indexCount2]
                indexCount2 += 1
            else:
                target[index] = targetToSort1[indexCount1]
                indexCount1 += 1

        return target

mergeSort = MergeSort()
randomlist = []
for index in range(0, 10):
    randomlist.append(random.randrange(0, 100))
print(randomlist)

mergeSortedRandomList = mergeSort.perform(randomlist)
print(mergeSortedRandomList)
