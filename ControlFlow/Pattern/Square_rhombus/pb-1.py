'''
PB-1 Write a program to print a square star(*) pattern series of N rows.

         *****
         *****
         *****
         *****
         *****
'''
num = int(input("Enter the number: "))
for i in range(num):
    print(num * "*")