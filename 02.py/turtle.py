import turtle

x= 20
def drawSquare(t, x):
    """Make turtle t draw a square of with side sz."""
    for i in range(4):
        t.forward(x)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

turtle=turtle.Turtle()
turtle.color('hotpink')
turtle.pensize(3)

for i in range(5):
    x=x+20
    drawSquare(turtle, x)  
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()
#ve dvojici s Jonášem Peichlem

