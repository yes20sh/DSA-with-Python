'''
2. Write a program to print hollow pyramid star pattern (*) pattern of N rows.

                                *
                               * *
                              *   *
                             *     *
                            *********
'''

n = int(input("Enter the n row: "))
for i in range(1, n+1):
    if i == 1:
        print(" "* (n-1)+ "*" * (i+(i-1)))
    elif  i == n:
        print("*" * (i+(i-1)))
    else:
        print(" "* (n-i) + "*" + " " * (i+(i-3))+ "*")