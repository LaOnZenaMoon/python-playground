class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def add(data):
    node = head

    while node.next:
        node = node.next

    node.next = Node(data)


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

for index in range(3, 11):
    add(index)

print(node1)

node = head
while node.next:
    print(node.data)
    node = node.next

print(node)
