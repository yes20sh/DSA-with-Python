# Check if there are two or three consecutive identical characters in a string.

def is_consecutive(value):
    c = ""
    consecutive = False
    for char in value:
        if c == char:
            consecutive = True
        else:
            c = char
    return consecutive

value = input()
if is_consecutive(value):
    print("Yes, it contain consecutive identical charactors")
else:
    print("No, it not contain consecutive identical charactors")

    