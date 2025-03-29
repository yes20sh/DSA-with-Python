'''
Write a program to print inverted Pyramid star pattern for N rows.

*********
 *******
  *****
   ***
    *  

'''

n = int(input("Enter the n row: "))
for i in range(n, 0, -1):
    print(" " * (n-i) + "*" * (i+(i-1)))