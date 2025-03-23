# Write a program to print Fibonacci series up to n terms using loop 

nth = int(input("Enter the nth term : "))

series = [0, 1]
for i in range(2, nth):
    series.append(series[-1] + series[-2])
print(series[:nth])