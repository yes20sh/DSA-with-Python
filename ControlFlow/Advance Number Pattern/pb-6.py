'''
Numeric Pattern questions

55555
44445
33345
22345
12345

'''
row, col = map(int, input("Enter the row & column : "). split())

if row != col:
    print("row and column not equal.")
else:
    for i in range(row, 0, -1):
        for j in range(1, col +1):
            print(max(i, j), end="")
        print()

    
