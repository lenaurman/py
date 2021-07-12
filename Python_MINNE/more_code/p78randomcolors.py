###

# inspired by
# https://holypython.com/turtle-spirals/

###

# import
import turtle
import random


turtle.colormode(255)
turtle.bgcolor(0,0,0)  # changes the background color

# defining colors using https://trinket.io/docs/colors
colors = ['dark slate blue', 'plum', 'light pink', 'dark orange', 'khaki', 'olive drab','sky blue','cornflower blue']

class Spirala:
    scolor = 'white'
    swidth = 3
    def __init__(self, scolor, swidth):
        self = turtle.Turtle()
        self.shape('circle')
        self.shapesize(0.5)  # make the cursor half the default size
        self.pencolor('white')
        self.speed('fastest')

        self.penup()
        self.setx(random.randrange(-200,200))
        self.sety(random.randrange(-200,200))
        self.pencolor(scolor)
        self.width(swidth)
        self.pendown()

        self.forward(120)
        for i in range(120):
    	       self.forward(17+i)
    	       self.left(30 - i/1.5)
#
#   def drawIt():
# -- end of Spirala class

###   Main      ###
#Drawing 3 spirals from random position
#for z in range(3):
#spiralaa = Spirala('plum',2)
spiralab = Spirala('khaki',4)
spiralac = Spirala('sky blue',6)

#spiralaa.drawIt()

turtle.done()
