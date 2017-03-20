# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

# Exercise Tri dit Un
#
import turtle

wn = turtle.Screen()

turtle_background_colour = input("What colour would you like the background to be? ")
tess_colour = input("What colour would you like the Tess to be? ")
tess_pen_width = int(input("What width would you like the pen to be? "))

wn.bgcolor(turtle_background_colour)
wn.title("Hello, Tess")
alex = turtle.Turtle()
alex.forward(50)
alex.left(90)
alex.forward(30)

tess = turtle.Turtle()
tess.color(tess_colour)
tess.pensize(tess_pen_width)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
