'''
Print box number pattern of 1s and 0s

11111
10001
10001
10001
10001
11111

'''

row, col = map(int, input("Enter the row & column : "). split())
for i in range(row):
    if i == 0 or i == row-1:
        print("1" * col)
    else:
        print("1" + "0" * (col -2) + "1")