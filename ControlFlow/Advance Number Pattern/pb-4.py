'''
Numeric Pattern questions

12345
12345
12345
12345
12345

'''

row, col = map(int, input("Enter the row & column : "). split())
for i in range(row):
    for j in range(1, col +1):
        print(str(j), end = "")
    print()
    