# a=input('请输入第一个数字：')
# b=input('请输入第二个数字：')
# c=input('请输入运算符：')
# print(eval(a+c+b))


# n=int(input('请输入一个数字n(n>=2):'))
# l=[1,3]
# if n<20:
#     for i in range(n-2):
#         l.append(l[-1]*l[-2])
# else:
#     for i in range(20-2):
#         l.append(l[-1]*l[-2])
# print(l)


# 元组
#()   有序且不能更改

# for i in t:
#     print(i)
# print(t[0])
# print(t[::2])



# t=('q','w','4')
# print(t)
# i=list(t)
# i[2]='a'
# l=tuple(i)     # tuple  将...改为元组
# print(l)



a=(2,4,6,8,10)
b=(14,16,18,20)
l=list(a)
l.append(12)
a=tuple(l)
c=a+b
print(c)