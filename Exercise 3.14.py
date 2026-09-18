# (Turtle: draw the Olympic symbol ) Write a program that prompts the user to
# enter the radius of the rings and draws an Olympic symbol of five rings of the
# same size with the colors blue, black, red, yellow, and green, as shown in
# Figure 3.5c

import turtle

turtle.pensize(2)

turtle.color("blue")
turtle.circle(100)
turtle.penup()

turtle.forward(225)
turtle.pendown()

turtle.color("black")
turtle.circle(100)
turtle.penup()

turtle.forward(225)
turtle.pendown()

turtle.color("red")
turtle.circle(100)
turtle.penup()

turtle.goto(110,-125)
turtle.pendown()
turtle.color("yellow")
turtle.circle(100)
turtle.penup()

turtle.forward(225)
turtle.pendown()
turtle.color("green")
turtle.circle(100)





turtle.done()
