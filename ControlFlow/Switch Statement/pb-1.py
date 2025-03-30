'''
Write a program to input week number(1-7) and print day of week name using switch case. Assume 1 is equivalent for Monday and 7 for Tuesday.

'''
num = input("Enter week number : ")
match num:
    case "1":
        print("Monday")
    case "2":
        print("Tuesday")
    case "3":
        print("Wednesday")
    case "4":
        print("Thursday")
    case "5":
        print("Friday")
    case "6":
        print("Saturday")
    case "7":
        print("Sunday")
    case _:
        print("Invalid input")

