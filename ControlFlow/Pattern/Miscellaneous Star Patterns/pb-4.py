'''
Write a program to print cross star pattern.

*       *
 *     *
  *   *
   * *
    *
   * *
  *   *
 *     *
*       *

'''

n = int(input("Enter the n row: "))
for i in range(n, 0, -1):
    if i == 1:
        print(" " * (n-i) + "*")
    else:
        print(" " * (n-i) +"*" + " " * (2 * i - 3) +"*")
for i in range(2, n + 1):
    print(" " * (n-i) + "*" + " " * (2 * i - 3) + "*" )

