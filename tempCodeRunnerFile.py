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

    print(f"{bfs.traversal(root)}")

if __name__ == "__main__":
    main()
