'''
Pattern 2

11111
2222
333
44
5

'''
n = int(input("Enter the n row : "))

for i in range(1, n+1):
    print(str(i) * (n-i+1))