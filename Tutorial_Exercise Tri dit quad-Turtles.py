# Example 3 dit hex
import turtle

wn = turtle.Screen()
wn_bgcolour = "lightgreen"

tess = turtle.Turtle()
tess_shape = "turtle"
tess_colour = "blue"
tess_size = 3
tess_increase = .3
tess_forward = tess_size
tess_right = 24
tess_steps = 800

tess.shape(tess_shape)
tess.color(tess_colour)
tess.penup()

for i in range(tess_steps):
    tess.stamp()
    tess_forward = tess_forward + tess_increase
    tess.forward(tess_forward)
    tess.right(tess_right)

tess_colour = "red"
tess.color(tess_colour)
wn.mainloop()

