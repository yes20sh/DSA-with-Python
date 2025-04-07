# Calculate the sum of each row and each column in a matrix.

mtr = [[1,2,3],
       [3,4,5],
       [67,8,9]]

for idx, num in enumerate(mtr):
    sumRow = sum(num)
    print(f"Row {idx+1} : {sumRow}")
        
for col in range(len(mtr[0])):
    colSum = 0
    for n in range(len(mtr)):
        colSum += mtr[n][col]
    print(f"Column {col+1} : {colSum}")

