# Find the maximum and minimum values in each row of a matrix.

mtr = [[1,2,3], [3,4,5], [67,8,9]]

for i in range(len(mtr)):
    min_val = float('inf')
    max_val = float('-inf')
    for j in range(len(mtr[i])):
        if mtr [i][j] > max_val:
            max_val = mtr[i][j]
        if mtr[i][j] < min_val:
            min_val = mtr[i][j]
    print(f"row {j+1} : min - {min_val} & max - {max_val}")


        

