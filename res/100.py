# import random
# a={1:'英格兰',2:'葡萄牙'}
# b={3:'中国',4:'美国'}
# c={5:'阿根廷',6:'荷兰'}
# d={7:'巴西',8:'伊朗'}
# print('八强战名单：')
# print(a);print(b);print(c);print(d)
# e={}
# e1={}
# print('战/1')
# print('四强战名单：')
# r=random.randint(1,2)
# if r in a:
#     e[r]=a[r]
# r1=random.randint(3,4)
# if r1 in b:
#     e[r1]=b[r1]
# r2=random.randint(5,6)
# if r2 in c:
#     e1[r2]=c[r2]
# r3=random.randint(7,8)
# if r3 in d:
#     e1[r3]=d[r3]
# print('赢:',e);print('赢:',e1)

# rx=r+r1
# rx1=r2+r3
# print('战/2')
# print('决战名单：')
# final={}
# jijun={}
# x=random.randint(1,2)
# e[rx]=e[r]
# e1[rx1]=e[r]
# del e[rx];del e1[rx1]
# for i,n in e.items():
#     if i==x:
#         final[x]=e[x]
# print('r1=',r1)
# x1=random.randint(3,4)
# print(x1)
# for m,i in e1.items():
#     if m==r1:
#         final[x1]=e1[x1]
# print('赢（参加最后决战）：',final)