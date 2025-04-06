# Find the number of trailing zeroes in the factorial of a given number n.

def trailing_zeros(n):
    count = 0
    pwr_5 = 5
    while n // pwr_5 > 0:
        count += n // pwr_5
        pwr_5 *= 5
    return count

n = int(input())
print(f"Number of trailing zeros in factorial {n} is {trailing_zeros(n)}")
