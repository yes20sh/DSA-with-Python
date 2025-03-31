# Find the minimum element in an array.

arr = list(map(int,input().split()))
min = arr[0]
for i in arr:
    if min >= i:
        min = i
print(f"Minimum element in array is {min}")
