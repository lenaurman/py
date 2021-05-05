# import 
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
    turtle.penup()            
    turtle.pencolor(random.randrange(0,33),random.randrange(0,77),random.randrange(150,200))
                # Random width
    turtle.width(random.randrange(2,13))
                # Random direction
    turtle.setheading(random.randrange(1,360))
    
    #turtle.color('red', 'yellow')
    turtle.begin_fill()
    print('Color: ', turtle.pencolor(), ' Heading: ', turtle.heading())
    
    turtle.pendown()
    for i in range(33):
        turtle.forward(20+i)
        turtle.left(30 - i/1.5)
    turtle.end_fill()
    #turtle.done()    

### Main code #######################################
#####################################################

# color mode & screen color
turtle.colormode(255) 
turtle.bgcolor(0,0,0)   # background color - black
turtle.pencolor(255, 200, 175)
turtle.speed(0) # turtle speed to slowest

# draw a spiral
spiralaa()
spiralaa()
spiralaa()
spiralaa()

# allow user to click           # for some action
turtle.onscreenclick(spiralaaa)

turtle.done()