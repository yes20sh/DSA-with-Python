'''
1
01
010
1010
10101

'''
n = int(input("Enter the n row: "))

for i in range(1, n+1):
    for j in range(i, i+i):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()