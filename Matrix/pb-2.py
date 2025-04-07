# Calculate the total sum of elements in a matrix.

mtr = [[1,2,3], [3,4,5], [67,8,9]]
total = 0
for n in mtr:
    for element in n:
        total += element
print(total)                                  