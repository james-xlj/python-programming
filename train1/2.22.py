# import turtle
# a = turtle.Turtle()
# a.circle(40)
# a.circle(-40)
# a.goto(80,0)
# a.circle(40)
# a.circle(-40)
# turtle.done()

# import turtle
# s=turtle.Turtle()
# # s.ht()
# s.up()
# s.goto(-100,0)
# s.begin_fill()
# for i in range(4):
#     s.fd(80)
#     s.lt(90)
# s.end_fill()
# s.fd(80)
# s.lt(90)
# s.begin_fill()
# for i in range(4):
#     s.fd(80)
#     s.rt(90)
# turtle.done()

a=int(input('请输入爸爸的身高：'))
b=int(input('请输入妈妈的身高：'))
c=int(input('请输入性别系数：'))
d=int((a+b+13*c)/2)
print('孩子未来的身高是：',d,'厘米')