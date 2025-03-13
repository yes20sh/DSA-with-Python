from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class ZigZag:
    def zig_zag_traversal(self, root):
        if not root:
            return []
        zigZag = []
        leftToRight = True
        queue = deque([root]) 
        while queue:
            current_level = deque()
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if leftToRight:
                    current_level.append(current.val)
                else:
                    current_level.appendleft(current.val)                
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            zigZag.append(list(current_level))
            leftToRight = not leftToRight
        return zigZag
                
 
def main():
    bfszz = ZigZag()
    bfszz.root = Node(1)
    root = bfszz.root
    bfszz.root.left = Node(2)
    bfszz.root.right = Node(3)
    bfszz.root.left.left = Node(4)
    bfszz.root.left.right = Node(5)
    bfszz.root.right.left = Node(6)
    bfszz.root.right.right = Node(7)
    bfszz.root.left.left.left = Node(8)
    bfszz.root.left.left.right = Node(9)


    print(bfszz.zig_zag_traversal(root))

if __name__ == "__main__":
    main()

                