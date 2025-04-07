# Find the maximum and minimum values in each column of a matrix.

mtr = [[1,2,3], [3,4,5], [67,8,9]]

for col in range(len(mtr[0])):
    min_val = float('inf')
    max_val = float ('-inf')
    for row in range(len(mtr)):
        if mtr[row][col] < min_val:
            min_val = mtr[row][col]
        if mtr[row][col] > max_val:
            max_val = mtr[row][col]
    print(f"Column {col + 1} : max {max_val} & min {min_val}")

