import turtle
import random


 class spiaratartle():
    ''''
    ''''
    x_pos
    y_pos
    color
    width

    def __init__:
        #
        x_pos = random.randrange(0,turtle.screensize[0]))
        y_pos = random.randrange(0,turtle.screensize[1]))
        color = (random.randrange(0,33),random.randrange(0,77),random.randrange(150,255)) 
        width = width(random.randrange(1,17))


def spiraTurtle():
    t = turtle.Turtle()
    t.forward(100)
    
    #t.pencolor(random.randrange(0,33),random.randrange(0,77),random.randrange(150,255))
    #print('Pencolor: ', t.pencolor())
    #t.color(20,20,0)
    #t.width(random.randrange(2,13))

    #print('Position: ', turtle.position())
    #s_x = turtle.screensize()[0]
    #s_y = turtle.screensize()[1]
    #print('S_X: ', s_x)
    
    #t.setx(random.randrange(0,s_x))

    #t.setposition(s_xx,100)
    #print('S_XX: ', s_xx)

    #print('New position: ', t.position())
    #print('ma kara')

    #t.pendown()
    t.left(90)
    t.forward(100)

    for i in range(33):
        t.forward(20+i)
        t.left(30 - i/1.5)

    #return t

### Main code #######################################
#####################################################

# color mode & screen color
turtle.colormode(255) 
turtle.bgcolor(0,0,0)   # background color - black
turtle.speed(0) # turtle speed to slowest

#print(turtle.screensize())

#s1 = spiraTurtle()
#s1.showturtle()
#s2 = spiraTurtle()

spi1 = spiaratartle()
spi2 = spiaratartle()


for i in range(33):
        spi1.forward(20+i)
        spi1.left(30 - i/1.5)
        spi2.forward(20+i)
        spi2.left(30 - i/1.5)

turtle.done()        
