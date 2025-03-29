# Write a program to input two numbers from the user and find HCF (Highest Common Factor) / GCD (Greatest Common Divisor).

import math

def hcf_inbuild(a, b):
    return math.gcd(a, b)

# without math.gcd
# while b:
#     a, b = b, a% b
# return a

def hcf_find(a, b):
    smaller = min(a, b)
    for i in range(smaller, 0, -1):
        if a % i == 0 and a % i == 0:
            return i
