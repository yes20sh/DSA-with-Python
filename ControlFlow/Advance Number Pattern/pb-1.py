'''
Numeric Square Patterns

11111
22222
33333
44444
55555

'''
row, col = map(int, input("Enter the row & column : "). split())
for i in range(1, row+1):
    print( str(i) * col)