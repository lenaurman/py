# https://github.com/AllenDowney/ThinkPython - page 36
import turtle
import math

def polyline(t, n, length, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them.  t is a turtle.
    """
    for i in range(n):
        t.forward(length)
        t.left(angle)

def square(t, length):
    """Draws a square with a given side length 
    """
    for i in range(4):
        t.forward(length)
        t.right(90)

def polygon(t, n, length):
    """Draws an n sides polygon with a given side length 
    """
    ang = 360/n
    for i in range(n):
        t.forward(length)
        t.right(ang)

def circle(t, r):
    """Draws aproximal circle with a given radius r 
    """
    circumference = 2 * math.pi * r
    n = 60
    side =  circumference / 60

    t.circle(r)
    t.pencolor('red')
    polygon(t, n, side)

def arc(t, radius, angle):
    """Draws aproximal arc with a given radius r 
    """
    circumference = 2 * math.pi * radius * angle / 360
    n = 60
    side =  circumference / 60

    print('Hello')
    t.circle(radius)
    t.pencolor('red')
    ang = angle/n
    for i in range(n):
        t.forward(side)
        t.left(ang)


def arc2(t, r, angle):
    """Draws aproximal arc with a given radius r 
    """
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    t.pencolor('green')
    
    polyline(t, n, step_length, step_angle)   


def spiral(t):
    for i in range(360):
        arc(t, 7*i, i)



#############
### Main
#############

# turtle.bgcolor(0,0,0)   # background color - black
#turtle.stamp()
t0 = turtle.Turtle()  
t1 = turtle.Turtle()  
t2 = turtle.Turtle() 
t3 = turtle.Turtle() 

## polyline
t0.penup()
t0.setposition(t0.position() + [-300, -200])
t0.pendown()
polyline(t0, 7, 70, 33)
t0.write('polyline, side = 70, angle = 33')
## 

## square
t1.penup()
t1.setposition(t1.position() + [-300, -70])
t1.pendown()
square(t1, 70)
t1.write('square, side = 70')
## 

## polygon 
polygon(t2, 6, 120)
t2.write('polygon (6 sided), side = 70')
##

## polygon 
t3.penup()
t3.setposition(t3.position() + [+300,-3])
t3.pendown()
t3.write('polygon (8 sided), side = 70')
polygon(t3, 8, 70)
##

#arc(t1, 40, 180)
#arc2(t2, 40, 180)
#t3.pencolor('black')
#t3.circle(40)

#spiral(t1)
turtle.done()