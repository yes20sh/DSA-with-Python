'''
Write a program to print Pyramid star( equilateral triangle ) pattern of N rows.

    *
   ***
  *****
 *******
*********

'''

n = int(input("Enter the n row: "))
for i in range(1, n+1):
    print(" " * (n - i)+ "*"* (i+(i-1)))