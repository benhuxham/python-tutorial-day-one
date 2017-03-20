# http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html

# Exercise Tri dit Un
#
import turtle

wn = turtle.Screen()


alex = turtle.Turtle()
tess = turtle.Turtle()

turtle_background_colour = "blue"
tess_colour = "red"
tess_pen_width = 5

tess.color(tess_colour)
tess.pensize(tess_pen_width)

wn.bgcolor(turtle_background_colour)
wn.title("Hello, Tess")

alex_right = 180
alex_left = 90
alex_forward = 50
alex_backward = 10

tess_right = 180
tess_left = 120
tess_forward = 80
tess_backward = 10

tess.forward(tess_forward)
tess.left(tess_left)
tess.forward(tess_forward)
tess.left(tess_left)
tess.forward(tess_forward)

alex.forward(alex_forward)
alex.left(alex_left)
alex.forward(alex_forward)
alex.left(alex_left)
alex.forward(alex_forward)
alex.left(alex_left)
alex.forward(alex_forward)
alex.left(alex_left)



wn.mainloop()
