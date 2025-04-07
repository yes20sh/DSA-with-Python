# Print the boundary elements of a matrix.

mtr = [[1,2,3],
       [3,4,5],
       [67,8,9]]

boundaries = []
n = len(mtr)
for i in range(n):
    if i == 0 or i == n - 1:
        for j in range(len(mtr[i])):
            boundaries.append(mtr[j][i])
    else:
        for j in range(len(mtr[i])):
            if j == 0 or j == len(mtr[i]) -1:
                boundaries.append(mtr[j][i])
print(boundaries)  
            
