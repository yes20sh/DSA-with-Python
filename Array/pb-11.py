# Check if two elements exist with a sum equal to a target value.

arr = list(map(int,input().split()))
sum = int(input("Enter the sum : "))

for i in range(len(arr) - 1):
    remain = sum - arr[i]
    if remain in arr:
        print(f"{arr[i]} & {remain} is array is equal to sum {sum}")
        break
else:
    print("Not Found")
