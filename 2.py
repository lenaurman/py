
# next step
# import
import turtle
import random

# color mode & screen color
turtle.colormode(255)
turtle.bgcolor(0,0,0)   # background color - black

def spirala(t):
    """
	Draws a spiral with a given tartle object (t)
	Starting point is random 
    Color is random blue
    Width is random
    """
    t.penup()
    t.setx(random.randrange(-200,200))
    t.sety(random.randrange(-200,200))
    t.pencolor(random.randrange(0,255),random.randrange(0,255),200)
    t.width(random.randrange(2,13))
    t.pendown()

    for i in range(120):
    	t.forward(20+i)
    	t.left(30 - i/1.5)
# -- end of spirala(t)

def turn(x,y):
    t2.left(90)
    t2.forward(77)

#####################
  ###   Main      ###
#####################

# init turtle
t1 = turtle.Turtle()
t1.speed(0)
t1.shape('circle')

t2 = turtle.Turtle()
t2.shape('turtle')
t2.pencolor('red')
t2.forward(100)
t2.onclick(turn)
t2.forward(200)


#t1.onclick(spirala)

#Drawing 3 spirals with random position, color and width
for z in range(3):
    spirala(t1)

# https://pythonprogramminglanguage.com/user-input-python/
#name = input("Enter a name: ")
#print(name)    

turtle.done()
