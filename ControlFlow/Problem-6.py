# Write a program to input a number and find the sum of first and last digit of the number using a for loop

num = int(input("Enter the number: "))
sum = 0
for i in range(num):
    sum += i
print(f"sum : {sum}")
