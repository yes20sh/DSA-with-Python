# Find the 2nd minimum element; if none, print -1.

# buildin function
def min_num(arr):
    if len(arr) <= 1:
        return -1
    else:
        return sorted(arr)[1]

# Using looping
def minimum_number(arr):
    if len(arr) <= 1:
        return -1
    else:
        firstNum, secondNum = float('inf'), float('inf')
        for num in arr:
            if firstNum > num:
                firstNum, secondNum = num, firstNum
            elif firstNum < num < secondNum:
                secondNum = num
        return secondNum


arr = list(map(int,input().split()))
if not minimum_number(arr):
    print("-1")
else:
    print(minimum_number(arr))