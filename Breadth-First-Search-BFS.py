from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BFS:
    def __init__(self):
        self.root = None
    
    def traversal(self, root):
        bfs = []
        if root == None:
            return bfs
        queue = deque([])
        queue.append(self.root)
        while len(queue) != 0:
            level_size = len(queue)
            current_level = []
            for i in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                if current.left != None:
                    queue.append(current.left)
                if current.right != None:
                    queue.append(current.right)
            bfs.append(current_level)
        return bfs



def main():
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

    print(f"{bfs.traversal(root)}")

if __name__ == "__main__":
    main()

