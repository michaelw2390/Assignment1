# (Turtle: draw a circle) Write a program that prompts the user to enter the
# center and radius of a circle, and then displays the circle and its area, as shown
# in Figure 2.5

import turtle



center = (eval(input("Enter the center of a circle: ")))
radius = (eval(input("Enter the radius of a circle: ")))

area = 3.14 * radius * radius

turtle.center = center
turtle.circle(radius)

turtle.penup()
turtle.goto(0,200)
turtle.write(area)



turtle.done()







