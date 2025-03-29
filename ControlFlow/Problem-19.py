# Write a program to find all Perfect numbers between 1 to n where n is the input given by the user.

def all_perfect_number(n):
    perfectNumbers = " "
    sum = 0
    for i in range(1, n):
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            perfectNumbers += str(i) + " "
        sum = 0
    return perfectNumbers

number = int(input("Enter the number: "))
print(all_perfect_number(number))

