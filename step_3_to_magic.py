import random
from turtle import *


### import turtle

#wn = turtle.Screen()
#wn.title('Chudesnye spirali')
#wn.bgcolor('black')
#wn.setup(width=800, height=600)
#wn.tracer()

#spirala1 = turtle.Turtle()
#spirala2 = turtle.Turtle()
#spirala3 = turtle.Turtle()

#spirala1.setposition(100,0)
#spirala2.setposition(0,0)
#spirala3.setposition(-100,0)

#spirala1.pencolor('red')
#spirala2.pencolor('green')
#spirala3.pencolor('blue')

#spirala1.forward(20)
#spirala2.forward(50)
#spirala3.forward(70)

#spirala1.onclick
#####################################


class Spirartle(Turtle):


    def __init__(self):
        """ Create a new Turtle as Spirala and rundomize it's 
            - starting position
            - pen color
            - width            
        """        
        Turtle.__init__(self,shape='circle')
        self.penup()
        """ set Color """
        rrr = random.randrange(0,255)
        ggg = random.randrange(0,77)
        bbb = random.randrange(110,255)
        color = (rrr, ggg, bbb)
        self.color(color) # set color        
        """ set Width """
        widthSpi = random.randrange(2,12)         
        self.width(widthSpi)
        """ be ready at your position"""
        xx = random.randrange(-1 * int(screen.canvwidth/2), int(screen.canvwidth)/2)
        yy = random.randrange(-1 * int(screen.canvheight/2), int(screen.canvheight)/2)
        self.goto(xx,yy) # positioning
        self.pendown()    

    def drawMe(self):
        """
        """
        for i in range(33):
            self.forward(20+1)
            self.left(30 - i/1.6)                

    def onclick(self):
        self.color = (200,0,0)
        self.setposition = self.position - 70
        self.drawMe()

    def myColor(self):
        return self.color       

#####################################
######################## Main 
width,height=600,600
    
screen = Screen()
screen.setup(width,height)
screen.delay(0)
screen.colormode(255)
screen.bgcolor(0,0,0)
screen.title ('Random color spirals')
#startx = -150
#starty = 150 


soii1 = Spirartle()
soii2 = Spirartle()
soii3 = Spirartle()
soii4 = Spirartle()
soii5 = Spirartle()
soii6 = Spirartle()
soii7 = Spirartle()

soii1.drawMe()
soii2.drawMe()
soii3.drawMe()

done()