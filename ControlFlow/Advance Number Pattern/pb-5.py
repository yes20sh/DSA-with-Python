'''
Numeric Square Patterns

55555
54444
54333
54322
54321

'''

row, col = map(int, input("Enter the row & column : "). split())

count = col
for i in range(row, 0, -1):
    for j in range(col, 0 , -1):
        if j == i:
            print(str(j) * j)
            break
        else:
            print(str(j), end="")
   
 