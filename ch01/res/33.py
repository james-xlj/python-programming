# n=[1,2,3,4,5,6,7]
# print(n[6:1:-1])
# print(n[1:6:-1])[]
# print(n[:2:-1])

# players=['姚明','张继科','林丹',['吴敏霞','全红婵','郭晶晶']]
# print(players[2::-2])
# print(players[3][::-1])
# print(players[::3])

# s1='hello world'
# for i in s1:
#     print(i)
# print(len(s1))

# eat='想吃 冰淇淋'
# print(eat[1])
# print(eat[-5])
# print(eat[3])
# print(eat[-3])


s='hello world! hello world!'
print(s.count('o'))
print(s.count(' ')+s.count('!'))

a=0
b=0
for i in s:
    if i==' ' or i=='!':
        a+=1
    elif i=='o':
        b+=1
print('空格以及特殊符号有',a,'个')
print('字符o有',b,'个')