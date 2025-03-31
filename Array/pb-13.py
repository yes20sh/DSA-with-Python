# Find the maximum element in an array.

arr = list(map(int,input().split()))
max = arr[0]
for i in arr:
    if max <= i:
        max = i
print(f"Maximum element in array is {max}")

