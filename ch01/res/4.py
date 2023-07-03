import turtle
import random
pen=turtle.Turtle()
pen.speed(0)
pen.ht()
pen.color('yellow')
turtle.setup(800,400)
turtle.bgpic('C:/codingai/sky.gif')
for i in range(45):
    x1=random.randint(-400,400)
    y1=random.randint(0,200)
    pen.up()
    pen.goto(x1,y1)
    pen.down()
    pen.begin_fill()
    for i in range(5):
        pen.forward(5)
        pen.right(144)   
    pen.end_fill()
for i in range(25):
    x2=random.randint(-400,400)
    y2=random.randint(0,200)
    pen.up()
    pen.goto(x2,y2)
    pen.down()
    pen.begin_fill()
    for i in range(5):
        pen.forward(10)
        pen.right(144)
    pen.end_fill()
turtle.done()









# import random
# a=random.randint(1,10)
# print(a)
# import turtle
# import random
# pen=turtle.Turtle()
# pen.ht()
# pen.speed(0)
# pen.color('red')
# for i in range(8):
#     x1=random.randint(-400,400)
#     y1=random.randint(0,200)
#     pen.up()
#     pen.goto(x1,y1)
#     pen.down()
#     pen.begin_fill()
#     for i in range(5):
#         pen.forward(50)
#         pen.left(90)
#         pen.forward(30)
#         pen.left(120)
#         pen.forward(60)
#         pen.right(138)
#     pen.end_fill()
# turtle.done()