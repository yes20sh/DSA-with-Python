'''
56789
4567
345
23
1

'''

n = int(input("Enter the n row : "))
for i in range(n, 0, -1):
    for j in range(i):
        print(i + j, end="")
    print()
