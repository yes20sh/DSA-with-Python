# Write a program to input a number from the user and calculate product of its digits. 

num = input("Enter the number : ")
product = 0
for i in num:
    product += int(i)
print(product)