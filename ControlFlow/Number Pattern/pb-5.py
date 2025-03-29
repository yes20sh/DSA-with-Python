'''
Print box number pattern with plus in center
Assumption: Input rows and cols can only be odd for the pattern to be printed correctly.

11011
11011
00000
11011
11011

'''

row, col = map(int, input("Enter the row & column : "). split())

for i in range (1, row + 1):
    if i== 1 or i == row or i % 2 == 0:
        for j in range(1, col+1):
            if j == 1 or j == col or j % 2 == 0:
                print("1", end="")
            else:
                print("0", end="")
        print()
    else:
        print("0" * col)
    



