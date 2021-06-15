class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class NodeManagement:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head

            while node.next:
                node = node.next

            insertedNode = Node(data)
            node.next = insertedNode
            insertedNode.prev = node
            self.tail = insertedNode

    def insert_before(self, data, before_data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.tail
            return True
        else:
            node = self.tail

            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False

            insertedNode = Node(data)
            beforeNode = node.prev
            beforeNode.next = insertedNode
            insertedNode.prev = beforeNode
            insertedNode.next = node
            node.prev = insertedNode
            return True

    def insert_after(self, data, after_data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            return True
        else:
            node = self.head

            while node.data != after_data:
                node = node.next
                if node == None:
                    return False

            insertedNode = Node(data)
            afterNode = node.next
            afterNode.prev = insertedNode
            insertedNode.prev = node
            insertedNode.next = afterNode
            node.next = insertedNode
            return True

    def search_from_head(self, data):
        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        return None

    def search_from_tail(self, data):
        node = self.tail

        while node:
            if node.data == data:
                return node
            else:
                node = node.prev

        return None

    def desc(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next


double_linked_list = NodeManagement(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()

node_search_from_head = double_linked_list.search_from_head(5)
print(node_search_from_head)
node_search_from_tail = double_linked_list.search_from_tail(3)
print(node_search_from_tail)

double_linked_list.insert_before(1.5, 2)
double_linked_list.desc()