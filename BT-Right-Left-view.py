from collections import deque
class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None
              
class BST:
    def right_view(self, root):
        if root == None:
            return
        view = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if i == size - 1:
                    view.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        return view
    
    def left_view(self, root):
        if root == None:
            return
        view = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if i == 0:
                    view.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
        return view
                        
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


    print(f"All Right view items : {bst.right_view(root)}")
    print(f"All Left view items : {bst.left_view(root)}")


if __name__ == "__main__":
    main()
