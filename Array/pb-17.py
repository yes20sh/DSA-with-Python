# Insert an element at the Xth position, shifting right.


def insert_element_2 (arr, element, pos):
        pos -= 1
        if len(arr) < pos or len(arr) == 0:
            return -1
        else:
            arr2 = arr[:pos] + [element] + arr[pos:]
            arr = arr2
            return arr



arr = list(map(int,input().split()))
element, pos = map(int,input("Enter the element & position : ").split())

if not insert_element_2(arr, element, pos):
    print("No 10th position in array")
else:
    print(f"After append : {insert_element_2(arr, element, pos)}")