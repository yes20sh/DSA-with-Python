''''
Write a program to print mirrored right triangle star pattern (*) pattern of N rows.

    *
   **
  ***
 ****
*****

'''

n = int(input("Enter the n row: "))
for i in range(1, n+1):
    print(" " * (n-i) + "*"*i)