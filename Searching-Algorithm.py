import random
# searching --------------------------------------------------------------
# Linear Search
def linear_search(arr, item):
    # Brute force
    # Time complexity : O(n)
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1 

# Binary Search 
def binary_search(arr, low, high, item):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr, low, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    return -1  

# Sorting ----------------------------------------------------------

def is_sorted(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

# Binary Sorting
def binary_sort(arr):
    n = len(arr)
    flag = 0
    for i in range(n):
            for j in range(n - i - 1):
                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    flag = 1
            if flag == 0:
                break
    return arr

def monkey_sort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
        print(arr)
    print(arr)

def Selection_sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min] , arr[i]
    return arr

def merged_sorted(arr1,arr2, arr):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] =  arr1[i]
            i +=1
        else:
            arr[k] =  arr2[j]
            j +=1
        k +=1
    while i < len(arr1):
        arr[k] =  arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] =  arr2[j]
        j += 1
        k += 1
    return

def merged_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merged_sort(left)
    merged_sort(right)

    merged_sorted(left, right, arr)


arr = [1,3,5,9,6,7]
print(linear_search(arr,6))
print(f"Array is sorted or Not  : {is_sorted(arr)}")
binary_sort(arr)
print(binary_search(arr,0, len(arr) -1,6))
print(f"Binary sorted : {arr}")

arr2 = [5,8,3,8,23]
# monkey_sort(arr2)
print(arr2)
print(f"Selection Sort : {Selection_sort(arr2)}")

arr3 = [4,7,5,9,2,6,7,8]
print(arr3)
merged_sort(arr3)
print(arr3)
