from collections import deque
class Node:
    def __init__ (self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
class BFS:
    def level_order_successor(self, root, key):
        if root == None:
            return
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if current.left != None:
                queue.append(current.left)
            if current.right != None:
                queue.append(current.right)
            if key == current.val:
                if queue:
                    return queue.popleft().val
                else:
                    return "No Successor"
        return "Invalid Key"

def main():
    key = int(input("Enter the key to find successor : "))

    bfs = BFS()
    bfs.root = Node(1)
    root = bfs.root
    bfs.root.left = Node(2)
    bfs.root.right = Node(3)
    bfs.root.left.left = Node(4)
    bfs.root.left.right = Node(5)
    bfs.root.right.left = Node(6)
    bfs.root.right.right = Node(7)
    bfs.root.left.left.left = Node(8)
    bfs.root.left.left.right = Node(9)


    print(f"The level order successor of {key} :  {bfs.level_order_successor(root,key)}")

if __name__ == "__main__":
    main()
