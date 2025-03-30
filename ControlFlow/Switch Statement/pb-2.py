'''
Write a program to input two numbers from user and find maximum between two numbers using switch case.
'''

num1, num2 = map(int,input("Enter the two number: ").split())

match num1 > num2:
    case True:
        print(f"Maximum number  {num1}")
    case False:
        print(f"Maximum number  {num2}")

