# Check if a matrix is symmetric.

def is_symmetric(mtr):
    n = len(mtr)
    m = len(mtr[0])
    for i in range(n):
        for j in range(m):
            if mtr[i][j] != mtr[j][i]:
                return False
        else:
            return True

# mtr = [[3,2,1,7],
#        [3,1,8,8],
#        [2,5,4,7],
#        [7,8,3,4]]

mtr = [[1,2,3],
       [2,4,5],
       [3,5,6]]

if is_symmetric(mtr):
    print("Yes")
else:
    print("No")