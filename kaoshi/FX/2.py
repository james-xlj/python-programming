# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))

# a = '123'
# print(a, end=' ')
# print('456', end=' ')
# print('789', end=' ')

# a=5
# b=3
# print(a,b)
# c=a
# a=b
# b=c
# print(a,b)
# a,b=b,a
# print(a,b)

# n=123
# m=True
# s='www'
# f=1.5
# print(type(n))
# print(type(m))
# print(type(s))
# print(type(f))

# print(200//7-12)
# print(98765//10000%1000-700)
# print(1223//(12*2))
# print(354**2*30)

# a = 'wwwssa'
# b = 122.4
# c = 233
# d = 'lkk'
# e = 3.4
# f = 65
# g = 2344
# s1 = a*g
# s2 = a+d
# s4 = a*f
# print(s1, s2, s4)

# num = input('请输入你的年龄：')
# print('你的年龄是：', num, '岁')

# st='[12,34,56]'
# print(type(st))
# lis=eval(st)
# print(lis)
# print(type(lis))

# 循环  for   while
# for i in range():   括号里写循环次数
# for i in range(5):
#     # 执行语句
#     print('我爱学python')
#     print(123)

# for循环中的变量
# for i in range(5):
# i:0.....4
# for i in range(5):
#     i=i+1
#     print(i)

# 灵活设置范围值
# for i in range(3,9):
#     print(i)
# 起始值，结束值，步长
# for i in range(3, 20, 3):
#     print(i)

# for循环与if语句的嵌套
# for i in range(10):
#     if i % 2 == 0:
#         print(i, '是偶数')
#     else:
#         print(i, '是奇数')

# 双重for循环
# import turtle
# import random
# t = turtle.Turtle()
# t.speed(0)
# t.color('red')
# for i in range(3):
#     x = random.randint(-100, 100)
#     y = random.randint(-100, 100)
#     t.up()
#     t.goto(x, y)
#     t.down()
#     for a in range(5):
#         t.forward(50)
#         t.right(144)
# turtle.done()

# while循环  既可以实现有限循环，也可以无限循环
# i = 0
# while i < 10:
#     i += 1
# print(i)

# s=0
# n=1
# while n<=10:
#     s=s+n
#     n+=1
# print('1到10的和是：',s)

n=1
while n<20:
    n+=1
    if n%2==0:
        continue
    print('奇数是',n)

# while True 无限循环(满足条件时，结束循环(break))
s=0
n=1
while 1:
    s=s+n
    if s>20:
        break
    n+=1
print('和大于20时,n的值是',n)