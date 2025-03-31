# Find the 2nd maximum element; if none, print -1.

# Buildin Method
def maximum_number(arr):
    if len(arr) <= 1:
        return -1
    else:
        return sorted(arr)[-2]

# with Loop
def maximum_num(arr):
    if len(arr) <= 1:
        return -1
    else:
        firstNum = secondNum = 0
        for i in arr:
            if firstNum < i:
                firstNum, secondNum = i, firstNum
            elif firstNum > i > secondNum:
                secondNum = i
        return secondNum
        


arr = list(map(int,input().split()))
if not maximum_num(arr):
    print("-1")
else:
    print(maximum_num(arr))