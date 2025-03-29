'''
Write a program to print 0s and 1s at alternate columns.

01010
01010
01010
01010
01010
01010

'''

row, col = map(int, input("Enter the row & column : "). split())

for i in range(row):
    for j in range(col):
        if j % 2 == 0:
            print("0", end="")
        else:
            print("1", end="")
    print()

    