# Count the total occurrences of the digit '1' in all positive integers less than or equal to a given integer n.

n = int(input("Enter n value : "))
count = 0
for i in range(n+1):
    for digit in str(i):
        if digit == "1":
            count += 1
print(count)
