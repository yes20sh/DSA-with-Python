# Generate Fibonacci numbers up to a given limit.

nth = int(input("Enter nth term: "))

st, pr = 0, 1
fib = []

while nth > 0:
    fib.append(str(st))
    st, pr = pr, st + pr  
    nth -= 1 

print(" ".join(fib))
