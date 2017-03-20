# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

# Exercise Tri dit Un
#
import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Hello, Tess")
alex = turtle.Turtle()

alex.forward(50)
alex.left(90)
alex.forward(30)

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
