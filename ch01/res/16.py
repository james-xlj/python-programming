# a=100
# b='100+10'
# print(a+eval(b))
# 转换程序 eval()
# num=input('请输入一个表达式：')
# print(eval(num))

print(367//100)
print(367%100//10)
print(367%100%10//1)
# for i in range(100,1000):
#     if i//100+i%100//10+i%10==5:
#         print('龙腾数'+str(i))

# import turtle
# pen=turtle.Turtle()
# pen.color('red')
# pen.speed(3)
# pen.ht()
# pen.up()
# pen.goto(0,-50)
# pen.down()
# for i in range(2):
#     pen.lt(60)
#     pen.fd(120)
#     pen.lt(60)
#     pen.fd(120)
#     pen.lt(60)
# turtle.done()

import turtle
pen=turtle.Turtle()
pen.pensize(2)
pen.color('red','yellow')
pen.ht()
pen.up()
pen.goto(0,-30)
pen.down()
pen.begin_fill()
for i in range(5):
    pen.rt(36)
    pen.fd(80)
    pen.lt(144)
    pen.fd(80)
    pen.rt(36)
pen.end_fill()
turtle.done()