'''
Write a program to print diamond star pattern for N rows.

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

'''

n = int(input("Enter the n row: "))
star = 0
for i in range(1,n*2):
    if i <= n:
        print(" " * (n-i) + "*" * (2 * i -1))
        star = (2 * i -1)
    else:
        star -= 2
        print(" " * (i - n) + "*" * star)
