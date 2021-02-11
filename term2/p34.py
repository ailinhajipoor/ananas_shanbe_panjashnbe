import turtle

def square():
    for i in  range(0,4):
        turtle.forward(100)
        turtle.left(90)

for i in range(0,36):
    square()
    turtle.left(10)

turtle.done()