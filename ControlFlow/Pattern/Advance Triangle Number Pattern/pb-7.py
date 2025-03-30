'''
1
23
345
4567
56789
'''

n = int(input("Enter the n row : "))

for i in range(1, n + 1):
    for j in range(i):
        print(i+j, end="")
    print()

