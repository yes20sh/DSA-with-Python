'''
Write a program to print 0s and 1s at alternate rows.

11111
00000
11111
00000
11111
00000

'''

row, col = map(int, input("Enter the row & column : "). split())

for i in range(0, row):
    if i % 2 == 0:
        print("1" * col)
    else:
        print("0" * col)
