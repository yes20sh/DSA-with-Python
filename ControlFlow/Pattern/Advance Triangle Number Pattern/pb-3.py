'''
Pattern

5
54
543
5432
54321


'''
n = int(input("Enter the n row : "))
for i in range(1, n+1):
    for j in range(i):
        print(n - j, end="")
    print()