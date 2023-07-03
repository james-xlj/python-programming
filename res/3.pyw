a = float(input('请输入体育场的宽：'))
b = float(input('请输入体育场的长：'))
c = a*b
d = 2*a+2*b
print('面积：', c, '周长:', d)

#
# a=input('请问在所有学科里，你最喜欢的学科是什么？？？')
# while 1:
#     if a=='编程':
#         print('同学，你非常机智呦！~')

# a=10
# b=5
# print(a<b and b)
# print(a<b or b)


# for i in range(5):

n = 1
while True:
    a = int(input('请输入一个数字：'))
    if a % 2 == 0:
        print('YES')
    else:
        print('NO')
    n += 1
    if n > 6:
        break
