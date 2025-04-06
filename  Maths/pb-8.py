# Calculate the factorial of a number.

def cal_factorial(num):
    total = 1
    for n in range(1, num + 1):
        total = total * n
    return total
        
num = int(input())
print(cal_factorial(num))
