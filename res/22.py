n=0
while n<100:
    n+=1
    if n==66:
        break
    print(n)

n=0
while n<100:
    n+=1
    if n==66:
        continue
    print(n)

# while True:
#     print('这里是外层循环')
#     n=int(input('请输入一个数字：'))
#     while n%2==0:
#         print('这里是内层循环')
#         print('偶数')
#         break
#         print('循环终止了，这句是不会输出的')

for i in range(101):
    if i%7==0 or i%10==7 or i//10==7:
        pass
        continue
    print(i)