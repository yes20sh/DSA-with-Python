'''
Write a program to print the inverted/mirrored rhombus star pattern of N rows.

*****
 *****
  *****
   *****
    *****

'''

n = int(input("Enter the n row : "))

for i in range(n):
    if i == 0:
        print("*" * n)
    else:
        print(" "*i+ "*"* n)