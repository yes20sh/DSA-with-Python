# Write a program into input a number and check whether the number is prime number or not using for loop
def is_prime(num):
    if num < 2:  
        return f"{num} is not a prime number" 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:  
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

num = int(input("Enter the number : "))
print(is_prime(num))
