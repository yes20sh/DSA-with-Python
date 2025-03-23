# Write a program to input two numbers from user and find LCM (Lowest Common Multiple).

import math

# Using inbuild function of math
def lcm_inbuild(n1, n2):
    # gcd : greatest common division
    # abs() ensures the result is positive, handling negative inputs.
    return abs(n1 * n2) // math.gcd(n1, n2) 

# lcm function
def lcm_find(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater +=1

n1, n2 = map(int, input().split())
print(f"LCM with inbuild function : {lcm_inbuild(n1, n2)}")
print(f"LCM without inbuild function : {lcm_find(n1, n2)}")

