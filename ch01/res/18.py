# day=1
# while day<=5:
#     print('今天是星期'+str(day))
#     day=day+1
# print('休息日')
# num=0
# while num<21:
#     print(num)
#     num=num+1

# import time
# boom=5
# while boom>0:
#     print('倒计时',boom,'秒')
#     time.sleep(1)
#     boom=boom-1
# print('BOOM!')
# 死循环
# n=0
# while True:
#     print(n)
#     n+=1
import random
num1=random.randint(0,100)
a=1
while a<=10:
    num2=int(input('请输入一个数字：'))
    if num2>num1:
        print('猜大了,你还有',10-a,'次机会')
    if num2<num1:
        print('猜小了，你还有',10-a,'次机会')
    if num2==num1:
        print('恭喜你,在第',10-a,'次猜对了')
        break
    a+=1