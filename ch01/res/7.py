
import turtle
import time
pen=turtle.Turtle()
pen.color('red')
pen.ht()
turtle.tracer(0)
for i in range(100):
    pen.begin_fill()  
    pen.left(45)
    pen.forward(120)
    pen.circle(60,180)
    pen.right(90)
    pen.circle(60,180)
    pen.forward(120)
    pen.left(45)
    pen.end_fill()
    turtle.update()
    time.sleep(0.6)
    pen.clear()
    pen.begin_fill()
    pen.left(45)
    pen.forward(90)
    pen.circle(45,180)
    pen.right(90)
    pen.circle(45,180)
    pen.forward(90)
    pen.left(45)
    pen.end_fill()
    turtle.update()
    time.sleep(0.6)
    pen.clear()
turtle.done()