# Write a program to input sides of a triangle and check whether a triangle is equilateral, scalene or isosceles triangle.

side1, side2, side3 = map(int, input().split())

if side1 == side2 == side3:
    print("Equilateral Triangle")
elif (side1 == side2 or side1== side3) or (side2 == side3):
    print("Scalene Triangle")
else:
    print("Isosceles Triangle")