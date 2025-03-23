# Write a program to input a number from user and find Prime factors of the given number using loop.

def check_prime(num):
    allPrime = ""
    for i in range(num):
        if i % num == 0:
            for i in range(2, int(num**0.5)+1):
                if i % num != 0:
                    allPrime += str(i) + " "
    return allPrime

            
number = int(input("'Enter the number : "))
print(check_prime(number))
