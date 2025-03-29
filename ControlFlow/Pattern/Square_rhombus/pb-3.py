'''
Write a program to print a hollow square star pattern with diagonals.

*****
** **
* * *
** **
*****

'''

def another_code():
    n = int(input("Enter the n term: "))
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 or i == j or j == n - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()



n = int(input("Enter the n term: "))

for i in range(1, n+1):
    if i == 1 or i == n:
        print("*"* n)
    elif i % 2 == 0:
        mid = n / 2
        print("*" * int(mid) + " " +"*"* int(mid))
    else:
        for i in range(n):
            if i % 2 == 0:
                print("*", end=" ")
        print()
    
