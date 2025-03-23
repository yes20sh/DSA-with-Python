# Print each element and its index in an array.

def print_element(arr):
    print(arr[0:])
    for i in arr:
        print(i, end=" ")

arr = [6,8,9,3,2]
print_element(arr)