'''
Write a program to print hollow right triangle star pattern (*) pattern of N rows.

*
**
* *
*  *
*****

'''

n  = int(input("Enter the n row: "))

for i in range(1, n+1 ):
    if i == 1 or i == 2 or i == n:
        print("*" * i)
    else:
        print("*" + " " * (i-2) + "*")


