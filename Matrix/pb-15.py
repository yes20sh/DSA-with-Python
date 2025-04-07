# check if a matrix is sparse (mostly zeroes).

def is_sparse_matrix(mtr):
    n = len(mtr)
    m =len(mtr[0])
    totalElement = 0
    totalZero = 0
    for i in range(n):
        for j in range(m):
            totalElement += 1
            if mtr[i][j] == 0:
                totalZero += 1
    sparse = totalElement / 2
    # print(f"Zero : {totalZero}, element : {totalElement}, sparse : {sparse}")
    if totalZero > sparse:
        return True
    else:
        return False

mtr = [[0,0,0],
       [0,5,0],
       [0,0,0]]

if is_sparse_matrix(mtr):
    print("Yes")
else:
    print("No")

