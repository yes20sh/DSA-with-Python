# Count occurrences of a target number in an array.

arr = list(map(int,input().split()))
targetNum = int(input("Enter the target number : "))
count = 0
for i in arr:
    if targetNum == i:
        count += 1
print(f"The occurences of target number in an array is {count}")