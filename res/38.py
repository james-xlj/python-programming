# 字典的查找
# a={'name':'jack','age':12,'gender':'girl'}
# if 'name' in a:
#     print('name的值为',a['name'])
# else:
#     print('没有记录')

# countries={'亚洲':'中国','欧洲':'美国'}
# country=countries.get('亚洲','马达加斯加')
# print(country)
# country=countries.get('非洲','马达加斯加')
# print(country)

# country=countries.get('欧洲')
# print(country)
# country=countries.get('非洲')
# print(country)

# a={'name':'jack','age':12,'gender':'girl'}
# age=a.get('age')
# print('jack的年龄：',age)
# gender=a.get('gender')
# print('jack的性别为',gender)


# dict1={}
# while True:
#     name=input('请输入你的姓名：')
#     if name=='stop':
#         break
#     book=input('请输入书籍名称：')
#     dict1[name]=book
# for i,m in dict1.items():
#     print(i,':',m)

subjects={'first':'语文','second':'数学','third':'英语'}
subjects['third']='政治'
subjects['fourth']='历史'
print(subjects)