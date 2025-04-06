# Check if a number is an Armstrong number.

def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    total = 0
    for i in num_str:
        total += int(i)**power 
    return num == total

num = int(input())
if is_armstrong(num):
    print("Yes")
else:
    print("No")