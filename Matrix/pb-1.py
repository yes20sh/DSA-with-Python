# Print a matrix row-wise and column-wise.

mtr = [[1,2,3], [3,4,5], [67,8,9]]
for i in mtr:
    for j in i:
        print(j, end=" ")
    print()