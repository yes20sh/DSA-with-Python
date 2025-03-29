# Write a Cprogram to input a number from the user and check whether the given number is an Armstrong number or not.
import math
def aramstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_digit = sum(int(digit) ** power for digit in num_str)
    return sum_of_digit == num
   

num = 371
if aramstrong_number(num):
    print(f"{num} is aramstrong number")
else:
    print(f"{num} is not aramstrong number")