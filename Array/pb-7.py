# Calculate sum and product of array elements.

arr = list(map(int,input().split()))
sum = 0
for i in arr:
    sum += i
print(f"Product of array elements is {sum}")