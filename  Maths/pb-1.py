# Perform basic, operations (addition, subtraction, multiplication, division) using two numbers.

num1, num2 = map(int, input("Enter two number : ").split())
choose = int(input('''
        1 -> Addition
        2 -> Subtraction
        3 -> Multiplication
        4 -> Division 
        choose : '''))

match (choose):
    case 1:
        print(num1 + num2)
    case 2:
        print(num1 - num2)
    case 3:
        print(num1 * num2)
    case 4:
        print(num1 / num2)