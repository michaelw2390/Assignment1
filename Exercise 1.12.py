#Turtle: draw four squares) Write a program that draws four squares in the center

import turtle

turtle.showturtle()

turtle.pendown()
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)

turtle.penup()
turtle.goto(100,200)

turtle.pendown()
turtle.forward(200)

turtle.penup()
turtle.goto(200,100)
turtle.right(90)

turtle.pendown()
turtle.forward(200)

turtle.penup()
turtle.goto(100,100)
turtle.left(90)


turtle.penup()


turtle.done()