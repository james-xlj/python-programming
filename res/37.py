# scores={'李华':99,'孙琪':97,'王华':95}
# for i,m in scores.items():
#     print(i+'的成绩是'+str(m))

# 字典的四种遍历方法：
# dict1={'one':1,'two':2,'three':3}
# 一：
# for i in dict1.keys():
#     print(i) 
# 二：
# for a in dict1.values():
#     print(a)
# 三：
# for i in dict1:
#     print(i) 
# 四：
# for m,i in dict1.items():
#     print('键',m,'值',i)

# 学校组织了一场天文知识竞赛，前三名学生的成绩如下：
# 第一名李华，99分
# 第二名孙琦，97分
# 第三名王华，95分
# 整理以上信息，以姓名:分数的形式统计,存储在字典scores
#1 从scores字典中取出前三名的姓名信息
#2 从scores字典中取出前三名的成绩信息 
# scores={'李华':99,'孙琪':97,'王华':95}
# for i in scores.keys():
#     print('名字：',i)
# for a in scores.values():
#     print('成绩：',a)

# box={'one':'工具','two':'文具','three':'药品'}
# box['one']='文具'
# box['two']='工具'
# print(box)

# numbers={336:'一年级',312:'二年级',330:'三年级'}
# numbers[312]='四年级'
# print(numbers)
# numbers[333]='二年级'
# print(numbers)

# d={}
# d['七年级']='张小鸣'
# d['八年级']='徐虹'
# d['九年级']='王申'
# print(d)

# name={'七年级': '张小鸣', '八年级': '徐虹', '九年级': '王申'}
# del name['九年级']
# print(name)
# del name

# d={}
# d['北京']='京'
# d['天津']='津'
# d['香港']='港'
# d['河北']='河'
# del d['河北']
# print(d)

a={'name':'jack','age':12,'gender':'girl'}
for i,m in a.items():
    print('key:',i,'value:',m)
a['height']='140'
print(a)
del a['age']
print(a)