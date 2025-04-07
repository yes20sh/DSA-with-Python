# Sort the matrix row-wise and column-wise.

mtr = [[3,2,1],
       [3,1,8],
       [2,5,4]]

n = len(mtr)
m = len(mtr[0])

for i in range(n):
    mtr[i].sort()

for i in range(n):
    col = [mtr[j][i] for j in range(n)]
    col.sort()
    for j in range(n):
        mtr[j][i] = col[j]

for row in mtr:
    print(row)
