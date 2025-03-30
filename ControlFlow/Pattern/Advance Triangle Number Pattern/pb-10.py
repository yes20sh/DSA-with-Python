'''
9
79
579
3579
13579

'''

n = int(input("Enter the n row: "))
for i in range(n-1, -1, -1):
    start = i * 2 + 1
    for j in range(n-i):
        print(start + 2 * j, end="")
    print()