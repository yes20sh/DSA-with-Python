'''
5
45
345
2345
12345

'''

n = int(input("Enter the n row : "))
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        print(n-j + 1, end="")
    print()