# print(3*2**2)
# print(9.0//2)
# print('161'>'17')
# '1'<'9'  True  
# '5'<'a'  True  
# 'A'<'a'  True
# 'z'>'a'  True

num=int(input('请输入一个数字:'))
if num%2==True:
    print('偶数：'+str(num))
elif num%2==False:
    print('奇数：'+str(num))