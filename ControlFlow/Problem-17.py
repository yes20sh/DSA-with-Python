# Write arogram to print all Armstrong numbers between 1 to n where n is the input given by the user.

def all_armstrong(start, end):
    armstrongs = " "
    for i in range(start, end):
        numStr = str(i)
        power = len(numStr)
        sumOfDigit = sum(int(digit) ** power for digit in numStr)
        if sumOfDigit == i:
            armstrongs += str(i) + " "
    return armstrongs

start, end = map(int, input("Enter the start and end : ").split())
print(all_armstrong(start, end))

