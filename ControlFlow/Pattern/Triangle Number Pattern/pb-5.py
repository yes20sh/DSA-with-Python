'''
Pattern

5
44
333
2222
11111

'''
n = int(input("Enter the n row : "))
for i in range(n, 0, -1):
    print(str(i) * (n - i +1))