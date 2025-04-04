# Convert uppercase to lowercase and vice versa in a string.

value = input()
choose = int(input('''
            1 - Uppercase
            2 = Lowercase
            choose Option : '''))
match choose:
    case 1:print(value.upper())
    case 2: print(value.lower())
    case _ : print("Invalid Input")

