'''
1
00
111
0000
11111

'''
n = int(input("Enter the n row: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print("0" * i)
    else:
        print("1" * i)