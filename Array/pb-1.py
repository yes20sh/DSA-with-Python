# Print each element and its index in an array.

arr = list(map(int,input().split()))
for idx, itm in enumerate(arr):
    print(f"Index {idx} and item {itm}")
