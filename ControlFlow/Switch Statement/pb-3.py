'''
Write a program to input number from user and check whether the number is even or odd using switch case.
'''

num = int(input("Enter the number : "))
match num % 2:
    case 1:
        print(f"{num} odd number")
    case 0:
        print(f"{num} even number")
