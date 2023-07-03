# animals=['dog','cat','bird','monkey','lion','elephant']
# print(animals[-1])
# 
# 使用列表绘制三色三角形。要求：画笔线条粗细为2，画笔速度为5。
# 列表存储三条边的颜色 
# import turtle
# a=turtle.Turtle()
# pen=['yellow','red','green']
# a.pensize(10)
# a.ht()
# a.up()
# a.goto(0,100)
# a.down()
# a.rt(60)
# for i in pen:
#     a.color(i)
#     a.fd(200)
#     a.rt(120)
# turtle.done()

# a=['第一名','第二名','第三名']
# b=['张三','李四','王五']
# for i in range(3):
#     print(a[i],':',b[i])

# a=[]
# for i in range(5):
#     b=input('请输入你要购买的商品：')
# a.append('牛奶')
# a.append('面包')
# a.append('牛肉')
#     a.append(b)
# print(a)
# print('够了！！！')

l=[1,1,2,3,5,8,13,21]
b=int(input('请输入一个数字：'))
for i in range(b):
    a=l[-1]+l[-2]
    l.append(a)
print(l)
    

