'''
Write a program to input vowels and print any word starting from that letter using switch case.

You can print any word, provided the starting letter should be the input as provided by the user.
Assumption: all inputs are in lower case.
'''

vowel = input("Enter vowel: ").lower()
match vowel:
    case "a":
        print("apple")
    case "e":
        print("english")
    case "i":
        print("ice cream")
    case "o":
        print("orange")
    case "u":
        print("up")
    case _:
        print("Not a vowel!")
