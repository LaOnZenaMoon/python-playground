from dataStructure.list.LinkedListNode import Node


class LinkedListManagement:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head

            while node.next:
                node = node.next

            node.next = Node(data)

    def delete(self, data):
        if self.head == "":
            print("해당 값을 가진 노드가 없습니다.")
            return

        # CASE1: Head 노드를 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        # CASE2: 중간, 마지막 노드 삭제
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                else:
                    node = node.next

    def search(self, data):
        node = self.head

        while node:
            if node.data == data:
                return node
            else:
                node = node.next

        return None

    def desc(self):
        node = self.head

        while node:
            print(node.data)
            node = node.next



linked_list1 = LinkedListManagement(0)
for data in range(1, 10):
    linked_list1.add(data)
linked_list1.desc()

linked_list1.delete(4)
linked_list1.desc()

linked_list1.delete(0)
linked_list1.desc()