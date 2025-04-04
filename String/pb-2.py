# Count letters, numbers, and special characters in a string.

value = input()
letter = number = specialCharactor = 0
for i in value:
    if i.isdigit():
        number += 1
    elif i.isalpha():
        letter += 1
    else:
        specialCharactor += 1

print(f"Letter : {letter}, number : {number}, special charactor : {specialCharactor}")



