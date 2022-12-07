import turtle
ninja = turtle.Turtle()
ninja.speed(2000000000000)


for i in range(180000):
    ninja.forward(10)
    ninja.backward(90)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(960)
    ninja.right(80)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(99)
turtle.done()    
