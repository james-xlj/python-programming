import turtle
pen=turtle.Turtle()
turtle.bgpic('C:/codingai/cake.png')
pen.color('pink')
pen.ht()
pen.right(90)
pen.up()
pen.goto(-150,150)
for i in '生日快乐':
    pen.write(i,font=('微软雅黑',20,'bold'))
    pen.forward(30)
pen.goto(130,150)
for i in '天天开心':
    pen.write(i,font=('微软雅黑',20,'bold'))
    pen.forward(30)
turtle.done()