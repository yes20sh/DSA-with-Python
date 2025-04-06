# Check if two numbers are co-prime.

def is_coprime(a, b):
    def gcd (x, y):
        while y:
            x, y = y, x % y
        return x
    return gcd(a,b) == 1

a, b = map(int, input("Enter two number : ").split())
if is_coprime(a, b):
    print(f"{a} & {b} is co-prime number.")
else:
    print(f"{a} & {b} is not co-prime number.")

