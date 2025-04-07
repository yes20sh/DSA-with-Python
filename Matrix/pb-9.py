# Find the inverse of a matrix.

def inverse_matrix(mtr):
    a, b = mtr[0]
    c, d =  mtr[1]
    det = (a * d) - (b * c)
    if det == 0:
        return "Inverse not exist"
    inverse = [[d / det, -b / det],
               [-c / det, a / det]]
    return inverse

mtr = [[4, 7],
       [2, 6]]

print(inverse_matrix(mtr))
