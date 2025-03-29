'''
Print circle box number pattern with 1 and 0

01110
10001
10001
10001
01110

'''

row, col = map(int, input("Enter the row & column : "). split())

for i in range(row):
    if i == 0 or i == row - 1:
        print("0" + "1" * (col -2) + "0")
    else:
        print("1" + "0" * (col - 2) + "1")