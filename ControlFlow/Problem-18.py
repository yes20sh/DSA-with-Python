# Write a program to input a number and check whether the number is a Perfect number or not. 

def is_perfect_number (num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i 
    return sum == num

number = int(input("Enter the number: "))
if is_perfect_number(number):
    print(f"{number} is perfect number.")
else:
    print(f"{number} is not perfect number.")
