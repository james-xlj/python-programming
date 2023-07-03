# import random
# num=1
# # a=random.randint(1,100)
# count=0
# while num<=100:
#     count=num+count
#     num+=1
# print(count)

money=2000
while money>=500:
    a=input('请输入你要购买的商品：')
    if a=='衣服':
        money-=300
        print('还剩',money,'元') 
    elif a=='玩具':
        money-=100
        print('还剩',money,'元')
    elif a=='零食':
        money-=300
        print('还剩',money,'元')
    elif a=='武器':
        money-=1000
        print('还剩',money,'元')
    else:
        print('暂时没有此商品！')
print('不要再买了！')


