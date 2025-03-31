# Print alternate elements of an array.

arr = list(map(int,input().split()))
for i in range(len(arr)):
    if i % 2 != 0:
        print(arr[i], end=" ")
print()