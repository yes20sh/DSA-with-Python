'''
1
10
101
1010
10101
'''

n = int(input("Enter the n row: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        if j % 2 == 0:
            print(0, end="") 
        else:
            print(1, end="") 
    print()
