# Write a Program to input a number from user and find all factors of the given number using for loop. 

number = int(input("Enter the number : "))
factors = " "
for i in range(2, number+1):
    if number % i == 0:
        factors += str(i) + " "
print(factors)

