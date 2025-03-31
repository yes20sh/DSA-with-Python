# Create two arrays: one for odd elements and one for even elements.

arr = list(map(int,input().split()))
odd = []
even = []

for i in arr:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Even array : {even}")
print(f"Odd Array : {odd}")