# Remove the first, last, and Kth character from a string


def remove_character(char, value):
    if char == value[0]:
        return value[1:]
    elif char == value[-1]:
        return value[:-1]
    else:
        for i in range(len(value)):
            if value[i] == char:
               value = value[:i] + value[i+1:]
               return value
        else:
            print("Invalid charactor")

value = input("Enter string : ")
char = input("Enter the charactor : ")
value = remove_character(char, value)
print(value)
