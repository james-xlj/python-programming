import random
print('大鳄鱼睡熟了Zzzzzzz........')
q=random.randint(1,10)
a=0
while True:
    l=input('请玩家抚摸鳄鱼：')
    a+=1
    if a==q:
        print('大鳄鱼睡醒了！！！',l,'号玩家被吃掉了！！！')
        break
