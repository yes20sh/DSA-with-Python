# Write a program to find power of a number using for loop

base, power = map(int,input("Enter the base and power : ").split())

numberPower = 0
i = 1
while i <= base:
    numberPower = i * power
    i+=1
print(numberPower)
