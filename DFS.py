from collections import deque

class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None

class DFS:
    def __init__(self):
        self.root = None

    def has_path(self, root, sum):
        if root == None:
            return False
        if root.val == sum and root.left == None and root.right == None:
            return True
        return self.has_path(root.left, sum - root.val) or self.has_path(root.right, sum - root.val)
    
    def sumPath(self, root, num = 0):
        if root == None:
            return 0 
        num = num * 10 + root.val
        if root.left == None and root.right == None:
            return num
        return self.sumPath(root.left, num) + self.sumPath(root.right, num)
    
    def find_sequance(self, root, sequance, index = 0):
        if root == None or index >= len(sequance) or sequance[index] != root.val:
            return False
        if root.left == None and root.right == None and sequance[index] == root.val:
            return True
        return self.find_sequance(root.left, sequance, index + 1) or self.find_sequance(root.right, sequance, index + 1)
    
    # Diameter finding 
    def find_diameter(self, root):
        diameter = 0  
        def find_height(node):
            nonlocal diameter
            if node is None:
                return 0
            leftHeight = find_height(node.left)
            rightHeight = find_height(node.right)
            diameter = max(diameter, leftHeight + rightHeight) 
            return max(leftHeight, rightHeight) + 1  
        find_height(root)  
        return diameter  

    # Maximum path
    def max_path(self, root):
        maxSum = 0
        def find_max_path(root):
            nonlocal maxSum
            if root is None:  
                return 0 
            leftSum = find_max_path(root.left)
            rightSum = find_max_path(root.right)
            leftSum = max(leftSum, 0)   # Ignore negative sums
            rightSum = max(rightSum, 0) # Ignore negative sums
            currSum = leftSum + rightSum + root.val  # Calculate path sum including current node 
            maxSum = max(maxSum, currSum)  # Update max sum 
            return max(leftSum, rightSum) + root.val  # Return max sum path including current node
        find_max_path(root)
        return maxSum

    # lowest common path between p and q
    def lowest_common_path(self, root, p, q):
        if root is None:
            return 0
        if root.val ==  p.val or root.val == q.val:
            return root
        left = self.lowest_common_path(root.left, p, q)
        right = self.lowest_common_path(root.right, p, q)
        if root.left != None and root.right != None:
            return root
        return left if left is not None else right

    # buring Tree
    def buring_tree(self, root,  targetNode):
        queue = deque([])
        def the_burning_tree(self, root, targetNode):
            if root is None:
                return 0
           # future to complete it     

    # merging two trees
    def merge_two_trees(self,root1,root2):
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        root1.val += root2.val
        root1.left = self.merge_two_trees(root1.left, root2.left)
        root1.right = self.merge_two_trees(root1.right, root2.right)
        return root1
    def traverse(self, root):
        if root is None:
            return 
        print(root.val, end=" ")
        self.traverse(root.left)
        self.traverse(root.right)
    
    
    # symmetric tree
    def is_symmetric_tree(self, root1, root2):
        def find_symmetric(root1, root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            return (root1.val == root2.val) and find_symmetric(root1.left, root2.right) and find_symmetric(root1.right, root2.left)
        return find_symmetric(root1, root2)
            
        

dfs = DFS()
dfs.root = Node(12)
root = dfs.root
dfs.root.left = Node(7)
dfs.root.left.left = Node(9)
dfs.root.left.left.left = Node(3)
dfs.root.right = Node(7)
dfs.root.right.left = Node(19)
dfs.root.right.right = Node(5)

print(dfs.has_path(root,23))
print(dfs.sumPath(root))

sequance = [12,7,9,3]

print(dfs.find_sequance(root,sequance))
print(dfs.find_diameter(root))
print(dfs.max_path(root))
p = dfs.root.left
q = dfs.root.right.right
print(dfs.lowest_common_path(root, p, q).val)
print(dfs.is_symmetric_tree(root, root))
new = dfs.merge_two_trees(root,root)
dfs.traverse(new)
print()
