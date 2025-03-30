'''
Pattern 

55555
4444
333
22
1

'''

n = int(input("Enter the n row : "))
for i in range(n, 0 , -1):
    print(str(i) * i)