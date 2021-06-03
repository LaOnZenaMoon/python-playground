from dataStructure.tree.TreeNode import TreeNode


class TreeNodeManagement:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = TreeNode(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = TreeNode(value)
                    break

    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right


head = TreeNode(1)
BST = TreeNodeManagement(head)
BST.insert(2)
BST.insert(3)
BST.insert(4)
BST.insert(4)
BST.insert(6)
BST.insert(10)
BST.insert(0)
BST.insert(9)

print(BST.search(10))
