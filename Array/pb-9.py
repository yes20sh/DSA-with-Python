# Check if an array is sorted forward, backward, or not at all.

arr = list(map(int,input().split()))
forward =  backward = True
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        forward = False
    elif arr[i] < arr[i + 1]:
        backward = False

if forward:
    print("Array is forward sorted")
elif backward:
    print("Array is backward sorted")
else:
    print("Array is not sorted")