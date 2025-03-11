def missing_num(arr):
    for i in range(max(arr)):
        if i  not in arr:
            return i
    return "all"




arr = [1,0,3]
print(missing_num(arr))