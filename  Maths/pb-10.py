# Find all divisors of a given number.

num = int(input("Enter the number : "))
divisor = ""
for n in range(1, num + 1):
    if num % n == 0:
        divisor += " " + str(n)
print(divisor)