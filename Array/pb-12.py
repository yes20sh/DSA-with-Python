# Check if three elements exist with a sum equal to a target value

arr = list(map(int,input().split()))
sum = targetValue = int(input("Enter the sum of three element : "))
ans = False

for i in range(len(arr)):
    sum -= arr[i]
    for j in range(len(arr)):
        element = sum - arr[j]
        if element in arr:
            print(f"{arr[i]}, {arr[j]} and {element} in array are the sum equal to {targetValue}")
            ans = True
            break
    if ans == True:
        break
else:
    print("Not found value.")
