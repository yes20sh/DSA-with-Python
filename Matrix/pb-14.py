# Check if a matrix is an identity matrix.

def is_identity(mtr):
    n = len(mtr)
    m = len(mtr[0])
    for i  in range(n):
        for j in range(m):
            if i == j and mtr[i][j] != 1:
                return False
            if i != j and mtr[i][j] != 0:
                return False
    return True

mtr = [[1,0,0],
       [0,1,0],
       [0,0,1]]

print("Is Identity Matrix:", is_identity(mtr))