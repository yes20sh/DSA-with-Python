'''
Write a program to print plus sign pattern.

    +
    +
    +
    +
+++++++++
    +
    +
    +
    +

'''
n = int(input("Enter the n row : "))
for i in range(1, n * 2):
    if i == n:
        print("+"* (n * 2 -1))
    else:
        print(" " * (n - 1) + "+")