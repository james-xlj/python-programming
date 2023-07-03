import turtle
pen=turtle.Turtle()
turtle.setup(800,400)
turtle.bgpic('C:/codingai/kite.gif')
pen.speed(0)
pen.ht()
pen.right(90)
pen.up()
for i in '村居':
    pen.write(i,font=('楷体',30,'bold'))
    pen.forward(45)
pen.goto(100,70)
for i in '草长莺飞二月天,':
    pen.write(i,font=('楷体',20,'bold'))
    pen.forward(30)
pen.goto(150,70)
for i in '拂堤杨柳醉春烟。':
    pen.write(i,font=('楷体',20,'bold'))
    pen.forward(30)
pen.goto(200,70)
for i in '儿童散学归来早,':
    pen.write(i,font=('楷体',20,'bold'))
    pen.forward(30)
pen.goto(250,70)
for i in '忙趁东风放纸鸢。':
    pen.write(i,font=('楷体',20,'bold'))
    pen.forward(30)
turtle.done()








# pen.color('red')
# pen.right(90)
# pen.ht()
# pen.up()
# pen.goto(-200,80)
# for i in '喜气常临和谐家':
#     pen.write(i,font=('楷体',20,'bold'))
#     pen.forward(30)
# pen.up()
# pen.goto(200,80)
# for i in '福星高照勤俭地':
#     pen.write(i,font=('楷体',20,'bold'))
#     pen.forward(30)
# pen.up()
# pen.goto(-50,150)
# pen.write('五福临门',font=('楷体',20,'bold'))
# turtle.done()



# cake