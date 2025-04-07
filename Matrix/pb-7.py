# Print the upper triangle and lower triangle of a matrix.

mtr = [[1,2,3],
       [3,4,5],
       [67,8,9]]

for row in range(len(mtr)):
    for col in range(row+1, len(mtr[row])):
        mtr[row][col] = 0

for row in mtr:
    for n in row:
        print(n, end=' ')
    print()


