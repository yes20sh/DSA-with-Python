#  Write a program to input number from user and check number is palindrome or not using loop.

def palindrome_slice(num):
    if num == num[::-1]:
        print(f"{num} is palindrone")
    else:
        print(f"{num} is not palindrone")

def palindrome_loop(num):
    reverse = ""
    for i in num:
        reverse = i + reverse
    if reverse == num:
        print(f"{num} is palindrone")
    else:
        print(f"{num} is not palindrone")

num = input("Enter the number : ")
palindrome_slice(num)
palindrome_loop(num)








