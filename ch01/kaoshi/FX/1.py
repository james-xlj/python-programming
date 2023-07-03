# import turtle
# a=turtle.Turtle()
# a.color('red')
# for i in range(6):
#     a.forward(50)
#     a.left(60)
# turtle.done()

# import turtle
# turtle.setup(500,400)
# turtle.screensize(500,400,'blue')
# turtle.up()
# turtle.goto(50,50)
# turtle.down()
# turtle.speed(0)
# turtle.pencolor('green')
# turtle.fillcolor('pink')
# turtle.done()

# import turtle
# turtle.pencolor('red')
# turtle.fillcolor('yellow')
# turtle.up()
# turtle.goto(-50,-30)
# turtle.down()
# turtle.speed(0)
# turtle.begin_fill()
# for i in range(5):
#     turtle.forward(35)
#     turtle.right(144)
# turtle.end_fill()
# turtle.done()

# import turtle
# 画圆circle(半径)
#     dot(直径)
# turtle.circle(60)
# turtle.dot(40)
# turtle.circle(40,120)
# turtle.circle(40,steps=10)
# turtle.circle(40,extent=180)
# turtle.done()
# 画弧

# import turtle
# turtle.bgpic('路径')
# turtle.bgcolor('purple')

# turtle.write('内容',font=('字体',字号,'加粗/倾斜'))
# turtle.clear()

import turtle
turtle.up()
turtle.goto(-50,100)
turtle.down()
turtle.write('山行',font=('楷体',30,'bold'))
turtle.up()
turtle.goto(-150,50)
turtle.down()
turtle.write('远上寒山石径斜，',font=('楷体',30,'bold'))
turtle.up()
turtle.goto(-150,0)
turtle.down()
turtle.write('白云深处有人家。',font=('楷体',30,'bold'))
turtle.up()
turtle.goto(-150,-50)
turtle.down()
turtle.write('停车坐爱枫林晚，',font=('楷体',30,'bold'))
turtle.up()
turtle.goto(-150,-100)
turtle.down()
turtle.write('霜叶红于二月花。',font=('楷体',30,'bold'))
turtle.done()