'''
Write a program to print right arrow star pattern.

*****
  ****
    ***
      **
        *
      **
    ***
  ****
*****

'''

n = int(input("Enter the n row: "))

for i in range(n):
    print(" " * (i * 2) + "*" * (n - i))

for i in range(n -1,0, -1):
    print(" " * ((i * 2) - 2) + "*" * (n - i + 1))  