# cakes=['奶油蛋糕','水果蛋糕','翻糖蛋糕']
# cakes[1]='冰淇淋蛋糕'
# print(cakes)

# 已知一个列表a，存储了1-50之间所有的偶数。请指出第10个偶数是几，并将其缩小2倍，最后输出列表a
# a=[]
# for i in range(2,51,2):
#     a.append(i)
# print(a[9])
# a[9]=a[9]//2
# print(a)

# a=[1,4,67,8,2,74,91]
# for i in range(len(a)):
#     if a[i]%2!=0:
#         a[i]=a[i]+1
# print(a)

# 已知列表a=[1,3,5,7,9,11,13],请将偶数下标的数字统一变大10倍，最后将a输出。
# a=[1,3,5,7,9,11,13]
# for i in range(0,len(a),2):
#     a[i]=a[i]*10
# print(a)


a = [1, 2, 3, 45, 76, 21, 98]
for i in range(len(a)):
    if i % 2 == 0:
        a[i] = a[i]-1
print(a)
print(a[4])
