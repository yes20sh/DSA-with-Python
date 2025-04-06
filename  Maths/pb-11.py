# Check divisibility rules for numbers from 1 to 20.

def is_divisible(n):
    div = ""
    for i in range(1, 21):
        if n % i == 0:
            div += str(i) + " "
    return div

n = int(input())
print(is_divisible(n))