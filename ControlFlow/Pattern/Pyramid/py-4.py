'''
Write a  program to print hollow inverted Pyramid star pattern for N rows.

*********
 *     *
  *   *
   * *
    *

'''

n = int(input("Enter the n row: "))
for i in range(n, 0, -1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("*" * (i + (i-1)))
    else:
        print(" " * (n - i) + "*" + " " * (i+(i - 3)) + "*")