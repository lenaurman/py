
# import
import turtle
import random

# changes the background color
turtle.colormode(255)
turtle.bgcolor(255,0,0)
turtle.shape("turtle")
#turtle.window_height()

# defining colors using https://trinket.io/docs/colors
colors = ['dark slate blue', 'plum', 'light pink', 'dark orange', 'khaki', 'olive drab','sky blue','cornflower blue']


# init turtle
a = turtle.Turtle()
a.shape('circle')
a.pencolor('white')

# changes the speed of the turtle
a.speed(0)

def spirala2(t,r,c):
    """
	Draws a spiral with a given tartle object (t), radius (r) and color(c).
	The starting point for the spirala will be random. """

    t.penup()
    t.setx(random.randrange(-200,200))
    t.sety(random.randrange(-200,200))
    t.pencolor(c)
    t.width(r)
    t.pendown()

    for i in range(120):
    	t.forward(20+i)
    	t.left(30 - i/1.5)
# -- end of pirala2(t,r,c)

###   Main      ###
#Drawing 7 spirals from random position
for z in range(7):
    spirala2(a,z*2,colors[z])

turtle.done()
