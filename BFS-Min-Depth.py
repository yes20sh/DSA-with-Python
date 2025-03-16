from collections import deque
class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
class BST:
    def min_depth(self, root):
        min_depth = 0
        if root == None:
            return min_depth
        queue = deque([root])
        while queue:
            min_depth += 1
            for i in range(len(queue)):
                current = queue.popleft()
                if current.left == None and current.left == None:
                    return min_depth
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        

def main():
    bst = BST()
    bst.root = Node(1)
    root = bst.root
    bst.root.left = Node(2)
    bst.root.right = Node(3)
    bst.root.left.left = Node(4)
    bst.root.left.right = Node(5)
    bst.root.right.left = Node(6)
    bst.root.right.right = Node(7)
    bst.root.left.left.left = Node(8)
    bst.root.left.left.right = Node(9)


    print(f"Minimum depth of BST is : {bst.min_depth(root)}")

if __name__ == "__main__":
    main()
