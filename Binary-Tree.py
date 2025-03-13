class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class Tree:
    def init (self):
        self.root = None
    
    def pre_order(self, root):
        result = ""
        if root == None:
            return
        print(root.data, end= ' ')
        self.pre_order(root.left)
        self.pre_order(root.right)
    
    def in_order (self, root):
        if root == None:
            return
        self.pre_order(root.left)
        print(root.data, end= ' ')
        self.pre_order(root.right)
      
    def in_order (self, root):
        if root == None:
            return
        self.pre_order(root.left)
        self.pre_order(root.right)
        print(root.data, end= ' ')
    
    def number_nodes(self, root):
        if root == None:
            return 0
        return 1 + self.number_nodes(root.left) + self.number_nodes(root.right)

    def leap_node(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.leap_node(root.left) + self.leap_node(root.right)

    def non_leap_node(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        return 1 + self.leap_node(root.left) + self.leap_node(root.right)

    def full_node(self, root):
        if root is None:
            return 0
        count = 0
        if root.left and root.right:
            count += 1
        count += self.full_node(root.left) + self.full_node(root.right)
        return count


tree = Tree()
tree.root = Node(1)
tree.root.right = Node(2)
tree.root.left= Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

root = tree.root


tree.pre_order(root)
print(f"\nNumber of Node in tree : {tree.number_nodes(root)}")
print(f"Number of leaf Node in tree : {tree.leap_node(root)}")
print(f"Number of non leaf Node in tree : {tree.non_leap_node(root)}")
print(f"Number of full node in binary tree : {tree.full_node(root)}")





