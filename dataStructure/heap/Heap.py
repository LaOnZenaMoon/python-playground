class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def moveNodeUp(self, index):
        if index <= 1:
            return False

        parent_index = index // 2
        if self.heap_array[index] > self.heap_array[parent_index]:
            return True

        return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        inserted_index = len(self.heap_array) - 1

        while self.moveNodeUp(inserted_index):
            parent_index = inserted_index // 2
            # Swap
            self.heap_array[inserted_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[inserted_index]
            inserted_index = parent_index

        return True

    def moveNodeDown(self, index):
        left_child_popped_index = index * 2
        right_child_popped_index = index * 2 + 1

        # Case 1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_index >= len(self.heap_array):
            return False

        # Case 2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_index >= len(self.heap_array):
            if self.heap_array[index] < self.heap_array[left_child_popped_index]:
                return True
            else:
                return False

        # Case 3: 왼쪽, 오른쪽 자식 노드가 모두 있을 때
        else:
            if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                if self.heap_array[index] < self.heap_array[left_child_popped_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[index] < self.heap_array[right_child_popped_index]:
                    return True
                else:
                    return False

        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        # array[-1] list 의 last 데이터
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]

        # root index
        popped_index = 1
        while self.moveNodeDown(popped_index):
            left_child_popped_index = popped_index * 2
            right_child_popped_index = popped_index * 2 + 1

            # Case 2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_index >= len(self.heap_array):
                if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                    self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[left_child_popped_index], self.heap_array[popped_index]
                    popped_index = left_child_popped_index

            # Case 3: 왼쪽, 오른쪽 자식 노드가 모두 있을 때
            else:
                if self.heap_array[left_child_popped_index] > self.heap_array[right_child_popped_index]:
                    if self.heap_array[popped_index] < self.heap_array[left_child_popped_index]:
                        self.heap_array[popped_index], self.heap_array[left_child_popped_index] = self.heap_array[left_child_popped_index], self.heap_array[popped_index]
                        popped_index = left_child_popped_index
                else:
                    if self.heap_array[popped_index] < self.heap_array[right_child_popped_index]:
                        self.heap_array[popped_index], self.heap_array[right_child_popped_index] = self.heap_array[right_child_popped_index], self.heap_array[popped_index]
                        popped_index = right_child_popped_index

        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print(heap.pop())
print(heap.heap_array)
