# (Geometry: area of a triangle) Write a program that prompts the user to enter the
# three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.
# The formula for computing the area of a triangle is
# area = 2s(s - side1)(s - side2)(s - side3)


side1,side2,side3 = eval(input("Enter three points for a triangle: "))

s = (side1 + side2 + side3) / 2
area = (s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is ", area)

