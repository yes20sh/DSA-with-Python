# Count seen and duplicate elements in an array (1-100).

def unique_and_duplicate(arr):
    duplicate = set()
    seen = set()
    for i in arr:
        if i in seen:
            duplicate.add(i)
        else:
            seen.add(i)
    unique_count = len(seen - duplicate)
    duplicate_count = len(duplicate)
    return unique_count, duplicate_count

arr = list(map(int,input().split()))
unique , duplicate = unique_and_duplicate(arr)
print(f"Unique element : {unique}")
print(f"Duplicate element : {duplicate}")