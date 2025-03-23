# Write a program to find maximum between three numbers. 

def max_between(n1 : int, n2 : int, n3: int):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

num1, num2, num3 = map(int,input().split())
print(max_between(num1, num2, num3))

