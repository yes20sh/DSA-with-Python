# Check if a number is a palindrome.

def is_palindrone(num):
    return num == num[::-1]

num = input()
if is_palindrone(num):
    print("Yes")
else:
    print("No")