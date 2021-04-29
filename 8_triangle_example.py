""" 

https://www.programmersought.com/article/8023688053/

rotated triangle .py , this program designed the Triangle class that inherits from the turtle.
Once the object is instantiated, you can drag it with the mouse pointer and it will rotate automatically. Right click on the screen and it will be home. """
 

from turtle import *
 
class Triangle(Turtle):
    counter = 0
    jec = 0
    def __init__(self,color,position):
        Turtle.__init__(self,shape='triangle')
        Self._initial_coordinates = position # record initial coordinates
        Self.shapesize(2,2) # Zoom in 2 times
        Self.penup() # Raise the pen
        Self.goto(position) # positioning
        Self.color(color) # set color
        Self.ondrag(self.goto) # 
        Self.rotate() # rotate
        Self.yspeed = 0 # vertical speed
        Self.aspeed = 0 # acceleration
        Triangle.counter +=1 # statistic quantity
        
    def rotate(self):
        """Rotation method"""
        self.right(2)
        screen.ontimer(self.rotate,10)
        
    def jump(self):
        Self.aspeed = -1 # acceleration is set to -1
        Self.yspeed = 15 # initial vertical speed set to 15
        Self.oldy = self.ycor() # record the initial y coordinate

    "The following functions are better not nested, and the reader can modify them themselves."
    def move():
        """ Let the object jump up under gravity"""
        
        Self.sety(self.ycor() + self.yspeed) # Move up
        
        If self.ycor() > self.oldy: # y coordinates are greater than the starting y coordinate
            Self.yspeed = self.yspeed + self.aspeed # yspeed change
            Self.screen.ontimer(move,50) # Continue to call move
        Else: # Otherwise it is down
            self.sety(self.oldy)
        
        "Because it is an asynchronous jump, it can be re-bound by judging whether or not all jumps are completed by counting."
        Triangle.jec +=1 # Jumped, statistics
        If Triangle.jec == Triangle.counter:# All jumps will equal the counter
            Self.screen.onkey(jump,"space") # rebind the spacebar to the jump
        
        move()       
        
    def reset(x,y):
        """ returns to the initial position, facing the right """
        [t.goto(t.initial coordinates) for t in screen.turtles()]
        [t.setheading(0) for t in screen.turtles()]
    
    def jump():
        """ Press the space bar to make all triangles jump """
        Screen.onkey(None,"space") # loose tie
        Triangle.jec = 0 # Start counting
        [t.jump() for t in screen.turtles()]
        
    
if __name__=="__main__":
     
    width,height=600,600
    colors = ["red","orange","yellow","green"]
    
    screen = Screen()
    screen.setup(width,height)
    screen.delay(0)
    screen.bgcolor("black")
         screen.title ( "rotation triangle _ Author: Li Xing Ball")
    startx = -150
    starty = 150 
    for row in range(4):
        for col in range(4):
            xcor = startx + col * 100
            ycor = starty - row * 100
            Triangle(colors[col],(xcor,ycor))

            
screen.onclick(reset,3)
screen.onkey(jump,"space")
screen.listen()
screen.mainloop()