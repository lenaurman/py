import turtle

wn = turtle.Screen()
wn.title('Chudesnye spirali')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer()

spirala1 = turtle.Turtle()
spirala2 = turtle.Turtle()
spirala3 = turtle.Turtle()

spirala1.setposition(100,0)
spirala2.setposition(0,0)
spirala3.setposition(-100,0)

spirala1.pencolor('red')
spirala2.pencolor('green')
spirala3.pencolor('blue')

spirala1.forward(20)
spirala2.forward(50)
spirala3.forward(70)

turtle.done()