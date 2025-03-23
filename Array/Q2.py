# Print elements of an array in reverse order

def reverse_print(arr:list):
    print(*arr[::-1])
    # for i in range(len(arr) -1, -1 , -1):
    #     print(arr[i], end=" ")
    # print()

arr = [4,6,9,3,4,6]
print(f"Original Array : {arr}")
reverse_print(arr)
