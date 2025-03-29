'''
Write a  program to print inverted right triangle star pattern (*) pattern of N rows.

*****
****
***
**
*

'''

n = int(input("Enter the n row: "))

for i in range(n):
    print("*" * (n-i))