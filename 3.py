# import package
import turtle
import random

### Functions ######################################
####################################################
def spiralaaa(x,y):
    turtle.penup() 
    turtle.setposition(x,y)
    turtle.pendown()
    spiralaa()
    
def spiralaa():
    """ Draws a spiral on a tartle Screen with random Starting point, Color and Width 
    """
                # Random color
    turtle.pencolor(random.randrange(0,111),random.randrange(0,77),200)
                # Random width
    turtle.width(random.randrange(2,13))
                # Random direction
    turtle.setheading(199)
    #turtle.setheading(random.randrange(1,70))
    turtle.pendown()
    for i in range(19):
    	turtle.forward(20+i)
    	turtle.left(30 - i/1.5)

### Main code #######################################
#####################################################

# color mode & screen color
turtle.colormode(255) 
turtle.bgcolor(0,0,0)   # background color - black
turtle.pencolor(255, 200, 175)
turtle.speed(1) # turtle speed to slowest

# draw a spiral
spiralaa()

# allow user to click           # for some action
turtle.onscreenclick(spiralaaa)

turtle.done()