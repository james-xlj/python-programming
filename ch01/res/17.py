


# a=int(input('请输入一个数字：'))
# m=a%60
# b=a//60//60
# c=a//60%60
# print(b,'时',c,'分',m,'秒')

for i in range(100,1000):
    # print(i)
    if i//100+i%100//10==13 and (i+7)%9==0 and (i+9)%7==0:
        print(i)