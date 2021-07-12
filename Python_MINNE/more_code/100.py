import turtle

turtle.screensize(400,400)
turtle.shape('circle')
turtle.speed(0)

# circle
turtle.penup()
turtle.sety(-400)
turtle.pendown()
turtle.circle(400, 405)  # draw a semicircle

# square
turtle.left(135)
turtle.forward(565)
turtle.right(90)
turtle.forward(565)
turtle.right(90)
turtle.forward(565)
turtle.right(90)
turtle.forward(565)

# triangle 
turtle.penup()
turtle.setposition(0,-133)
turtle.setheading(60)
turtle.pendown()
turtle.forward(303)
turtle.left(120)
turtle.forward(303)
turtle.left(120)
turtle.forward(303)

# flowers

turtle.penup()
turtle.setposition(-400,0)
turtle.pendown()
turtle.setheading(222)
turtle.circle(222,57)

turtle.penup()
turtle.setheading(89)
turtle.setposition(-383,-373)
turtle.pendown()
turtle.circle(222,56)

turtle.penup()
turtle.setposition(-283,-283)
turtle.pendown()

turtle.done()