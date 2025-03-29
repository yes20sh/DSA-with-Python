'''
Print chessboard number pattern with 1 and 0

10101
01010
10101
01010
10101

'''
row, col = map(int, input("Enter the row & column : "). split())
for i in range(row):
    for j in range(col):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

 