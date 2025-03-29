'''
Write a program to print a hollow square star(*) pattern series of N rows.

*****
*   *
*   *
*   *
*****

'''

num = int(input("Enter the number: "))

for i in range(num):
    if i == 0 or i == num - 1:
        print("*" * num)  
    else:
        print("*" + " " * (num - 2) + "*")  
