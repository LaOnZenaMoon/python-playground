from SingleLinkedList import SingleLinkedList


class Stack(object):

    instance1st = SingleLinkedList()

    def pop(self):
        return self.instance1st.removeAt(0)

    def push(self, value):
        self.instance1st.insertAt(value, 0)

stack = Stack()
stack.push('1')
stack.push('2')
stack.push('3')

print(stack.pop().getValue())
print(stack.pop().getValue())
print(stack.pop().getValue())