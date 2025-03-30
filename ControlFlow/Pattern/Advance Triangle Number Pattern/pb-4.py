'''
Pattern

54321
5432
543
54
5

'''

n = int(input("Enter the n row : "))
for i in range(n, 0, -1):
    for j in range(i):
        print(n-j, end="")
    print()