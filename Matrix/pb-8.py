# Print the left and right diagonals of a matrix.

mtr = [[9,2,3],
       [3,4,5],
       [67,8,9]]

n = len(mtr)

print("Left Diagonals ")
for i in range(n):
    print(mtr[i][i], end=" ")
print()

print("Right Diagonal")
for i in range(n):
    print(mtr[i][n - i -1], end=" ")
print()