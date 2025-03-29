'''
Numeric Square Patterns

12345
23456
34567
45678
56789

'''

row, col = map(int, input("Enter the row & column : "). split())
for i in range(row):
    for k in range(1,col + 1):
        print(i+k, end="")
    print()