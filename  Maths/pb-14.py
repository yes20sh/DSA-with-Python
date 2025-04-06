# Check if a number is prime without using the Sieve of Eratosthenes.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if i % n == 0:
            return False
        i += 2
    return True

n = int(input())
if is_prime(n):
    print(f'{n} is prime number.')
else:
    print(f"{n} is not prime number.")
