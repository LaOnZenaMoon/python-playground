from SingleLinkedList import SingleLinkedList


class Queue:

    instance1st = SingleLinkedList()

    def enqueue(self, value):
        self.instance1st.insertAt(value, self.instance1st.getSize())

    def dequeue(self):
        dequeueValue = self.instance1st.get(0)
        self.instance1st.removeAt(0)
        return dequeueValue

test = Queue()
test.enqueue("a")
test.enqueue("b")
test.enqueue("c")

print(test.dequeue().getValue())
print(test.dequeue().getValue())
print(test.dequeue().getValue())