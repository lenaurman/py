
import turtle
playGround = turtle.Screen()
playGround.screensize(500, 500)
playGround.title("Turtle Keys")

shape1 = turtle.Turtle()
shape2 = turtle.Turtle()

shape1.shape('circle')
shape2.shape('circle')

shape1.color("blue")
shape2.color("red")

run.penup()
follow.penup()

run.st()

def k1():
    run.forward(45)
def k2():
    run.left(45)
def k3():
    run.right(45)
def k4():
    run.back(45)
def quitThis():
    playGround.bye()
playGround.onkey(k1, "Up")  # the up arrow key
playGround.onkey(k2, "Left") # the left arrow key
playGround.onkey(k3, "Right") # you get it!
playGround.onkey(k4, "Down")
playGround.onkey(quitThis,'q')
playGround.listen()


#playGround.done()
turtle.done()        
