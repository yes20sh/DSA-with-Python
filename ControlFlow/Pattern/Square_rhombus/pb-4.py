'''
Write a program to print a rhombus star pattern of N rows.

    *****
   *****
  *****
 *****
*****

'''

n = int(input("Enter the n row:"))
for i in range(n):
    print(" "* (n-i-1) + "*"*n)