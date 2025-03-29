'''
Print box number pattern of 1 and 0 with cross center
Assumption: Input rows and cols can only be odd for the pattern to be printed correctly.

10001
01010
00100
01010
10001

'''
row, col = map(int, input("Enter the row & column : "). split())

if row % 2 == 0 or col % 2 == 0:
    print("Enter odd number.")
else:
    for i in range(col):
        for j in range(col):
            if i == j or i + j == row - 1:
                print("1", end="")
            else:
                print("0", end="")
        print()
