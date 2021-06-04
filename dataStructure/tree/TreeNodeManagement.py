import random

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

        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        # Case 1
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

            del self.current_node

        # Case 2
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right

        # Case 3
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent_node.value:
                self.change_node = self.current_node.right
                self.change_node_parent_node = self.current_node.right

                while self.change_node.left != None:
                    self.change_node_parent_node = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right != None:
                    self.change_node_parent_node.left = self.change_node.right
                else:
                    self.change_node_parent_node.left = None

                self.parent_node.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
            else:
                self.change_node = self.current_node.right
                self.change_node_parent_node = self.current_node.right

                while self.change_node.left != None:
                    self.change_node_parent_node = self.change_node
                    self.change_node = self.change_node.left

                if self.change_node.right != None:
                    self.change_node_parent_node.left = self.change_node.right
                else:
                    self.change_node_parent_node.left = None

                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right



head1 = TreeNode(1)
BST1 = TreeNodeManagement(head1)
BST1.insert(2)
BST1.insert(3)
BST1.insert(4)
BST1.insert(4)
BST1.insert(6)
BST1.insert(10)
BST1.insert(0)
BST1.insert(9)

print(BST1.search(10))

BST1.delete(10)

print(BST1.search(10))


bst2_nums = set()
while len(bst2_nums) != 100:
    bst2_nums.add(random.randint(0, 999))

head2 = TreeNode(500)
BST2 = TreeNodeManagement(head2)
for num in bst2_nums:
    BST2.insert(num)

for num in bst2_nums:
    if BST2.search(num) == False:
        print('search failed', num)

delete_bst2_nums = set()
bst2_nums_list = list(bst2_nums)
while len(delete_bst2_nums) != 10:
    delete_bst2_nums.add(bst2_nums_list[random.randint(0, 99)])

for del_num in delete_bst2_nums:
    if BST2.delete(del_num) == False:
        print('delete failed', del_num)
