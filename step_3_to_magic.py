### import 
import random
from turtle import *

### Class  Spirartle inherits Turtle
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
        self.width(random.randrange(2,12))
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
       # self.setposition = self.position - 70
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

screen.listen()

s1 = Spirartle()
s2 = Spirartle()
s3 = Spirartle()
s4 = Spirartle()
#s5 = Spirartle()
#s6 = Spirartle()
#s7 = Spirartle()


s1.drawMe()
s2.drawMe()

screen.listen()
screen.mainloop()

screen.onclick(s1.drawMe())

screen.onclick(s3.drawMe())

#done()