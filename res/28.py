# list=[666,'66',66,'6666','6','66666',6666]
# print(66 in list)
# print('666' in list)

# list=[666,'66',66,'6666','6','66666',6666]
# if 66 in list:
#     print('yes')
# else:
#     print('no')

# l=[1,2,3,[12,'345',5.6],4,5,6]
# for i in l:
#     print(i)
# print(len(l))
# print(l[3][1])

# l=[1,[2,3],[12,'345',5.6],4,[5,6]]
# print(l[1][0])
# print(l[2][2])
# print(l[4][1])

# list=[[1,2,3],[3,2,1],[4,5,6]]
# for i in list:
#     for x in i:
#         print(x,end='')

# 一个学校，3间办公室，现在有8位老师需要分配工位。
#先在完成一个程序，完成工位随机分配
#提示：
# 1使用列表表示办公室[[][][]]
# 2字母A B C -H表示8位老师 
# import random
# a=[[],[],[]]
# b=['A','B','C','D','E','F','G','H']
# for i in b:
#     index=random.randint(0,2)
#     a[index].append(i)
# print('一号办公室的教师有：',a[0])
# print('二号办公室的教师有：',a[1])
# print('三号办公室的教师有：',a[2])

import random
a=[[],[],[]]
b=['A','B','C','D','E','F','G','H']
for i in b:
    index=random.randint(0,2)
    a[index].append(i)
i=1
for o in a:
    print('办公室',i,'有',len(o),'人')
    i+=1
    print(o)

