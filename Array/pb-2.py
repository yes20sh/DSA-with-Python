# Print elements of an array in reverse order.

arr = list(map(int,input().split()))
for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=" ")
print()