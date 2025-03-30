'''
13579
3579
579
79
9

'''

n = int(input("Enter the n row : "))
for i in  range(n):
    start = 2 *i + 1
    for j in range(n-i):
        print(start + 2 * j, end="")
    print()

