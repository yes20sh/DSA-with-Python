'''
12345
2345
345
45
5

'''
n = int(input("Enter the n row : "))

for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(n - j + 1, end="")
    print()