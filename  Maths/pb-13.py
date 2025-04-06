# Calculate the LCM and GCD of two numbers.
import math

def cal_gcd(a, b):
    return math.gcd(a, b)

def cal_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

a, b = map(int,input("Enter two numbers : ").split())
print(f"LCM : {cal_lcm(a,b)}")
print(f"GCD : {cal_gcd(a, b)}")
