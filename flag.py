
import turtle
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

flag_turtle = turtle.Turtle()
flag_turtle.speed(0)
flag_turtle.penup()
flag_turtle.goto(-250, 150)
flag_turtle.pendown()
flag_turtle.color("Orange")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

flag_turtle.penup()
flag_turtle.goto(-250, 50)
flag_turtle.pendown()

flag_turtle.color("white")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()

flag_turtle.penup()
flag_turtle.goto(-250, -50)
flag_turtle.pendown()

flag_turtle.color("green")
flag_turtle.begin_fill()
for _ in range(2):
    flag_turtle.forward(500)
    flag_turtle.right(90)
    flag_turtle.forward(100)
    flag_turtle.right(90)
flag_turtle.end_fill()



flag_turtle.penup()
flag_turtle.goto(2, -15)
flag_turtle.pendown()

flag_turtle.color("navy")
flag_turtle.pensize(3)
flag_turtle.circle(20)

for _ in range(24):
    flag_turtle.penup()
    flag_turtle.goto(0, 4)
    flag_turtle.setheading(-15 * _)
    flag_turtle.forward(20)
    flag_turtle.pendown()
    flag_turtle.forward(20)
    flag_turtle.penup()
    flag_turtle.goto(0, 25)
flag_turtle.hideturtle()
turtle.done()
