# Add and subtract two matrices.

a = [[71,2,33],[4,5,6],[57,8,9]]
b = [[9,68,7],[6,15,4],[3,52,51]]

add = []
for  i in range(len(a)):
    temp = []
    for j in range(len(a[i])):
        total = a[i][j] + b[i][j]
        temp.append(total)
    add.append(temp)

substract = []
for  i in range(len(a)):
    temp = []
    for j in range(len(a[i])):
        total = a[i][j] - b[i][j]
        temp.append(total)
    substract.append(temp)

print("Addition : ",add)
print("Substract : ", substract)

