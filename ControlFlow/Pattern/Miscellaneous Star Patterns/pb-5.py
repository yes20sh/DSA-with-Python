''''
Write a program to print 8 star pattern of N rows.

 ***
*   *
*   *
*   *
 ***
*   *
*   *
*   *
 ***

'''
n = int(input("Enter the n row : "))

for i in range(0, n):
    if i == 0 or i == n-1:
        print(" " + "*" * (n - 2) + " ")
    else:
        print("*" + " " * (n -2) + "*")
for i in range( 1, n):
    if i == n-1:
        print(" " + "*" * (n - 2) + " ")
    else:
        print("*" + " " * (n -2) + "*")
