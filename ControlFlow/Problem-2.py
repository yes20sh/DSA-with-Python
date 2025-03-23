# Write a program to input a character from user and check whether given character is alphabet, digit or special character.

char = input("Enter the charactor : ")
if char.isdigit():
    print(f"{char} is digit")
elif char.isalpha():
    print(f"{char} is charactor")
else:
    print(f"{char} special charactor")