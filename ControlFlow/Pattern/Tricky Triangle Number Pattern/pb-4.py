'''
1
11
101
1001
11111

'''
n = int(input("Enter the n row: "))
for i in range(n):
    if i == 0 or i == 1 or i == n-1:
        print("1" * (i + 1))
    else:
        print("1" + "0" * (i-1) + "1")