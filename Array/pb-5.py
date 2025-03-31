# Delete an element at the Xth position, shifting left

def delete_element(arr, pos):
    pos -= 1
    if len(arr) < pos or len(arr) == 0:
        return -1
    else:
        arr2 = arr[:pos] + arr[pos+1:]
        arr = arr2
        return arr

arr = list(map(int,input().split()))
pos = int(input("Enter the position: "))
if delete_element(arr, pos):
    print("deleted successfully")
    arr = delete_element(arr, pos)
else:
    print("Invalid")
print(arr)
