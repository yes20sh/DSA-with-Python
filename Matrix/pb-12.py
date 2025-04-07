# Print the matrix in a zig-zag pattern


mtr = [[3,2,1,7],
       [3,1,8,8],
       [2,5,4,7],
       [7,8,3,4]]

n = len(mtr)
m = len(mtr[0])
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            print(mtr[j][i], end= " ")
        print()
    else:
        for j in range(m-1, -1, -1):
            print(mtr[i][j], end = " ")
        print()
    