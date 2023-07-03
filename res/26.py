# purses=['五十元','一百元','二十元','一百元']
# print(purses.index('二十元'))
# print(purses.index('一百元'))
# print(purses.index('一百元',2,4))


# a=[]
# for i in range(1,101,2):
#     a.append(i)
# b=a.index(61)
# print(b)
# print('数字61是列表中的第',b+1,'个数字')

# sheeps=['sheep1','sheep2','sheep3','sheep4']
# sheeps.insert(2,'sheep5')
# print(sheeps)

# cats=['白猫','花猫','黑猫']
# cats.pop(1)
# print(cats)


# c=['白猫','花猫','黑猫','灰猫']
# c.pop()
# print(c)

# cats=['白猫','花猫','黑猫']
# cats.remove('花猫')
# print(cats)


# c=['白猫','花猫','黑猫','白猫']
# c.remove('白猫')
# print(c)

# from unittest.util import _count_diff_all_purpose


# colors=['red','yellow','green','blue']
# del colors[2]
# print(colors)
# del colors

# from turtle import clear


# colors=['red','yellow','green','blue']
# colors.clear()
# print(colors)

numbers = ['你好', 'hello', 23, 43, 21, 45, 76, 87, 'o', 23, 12]
string = []
num = []
num2=[]
for i in range(len(numbers)):
    if type(numbers[i]) == str:
        string.append(numbers[i])
    else:
        if numbers[i] % 3 == 0 and numbers[i] % 7 != 0:
            num.append(numbers[i])
        else:
            num2.append(numbers[i])
print(num)
print(string)
print(num2)


# numbers=[12,45,66,76,22,43,47,32,76,98,97] 遍历列表   将偶数放在一个列表中，奇数放在一个列表中
# numbers = [12, 45, 66, 76, 22, 43, 47, 32, 76, 98, 97]
# num1 = []
# num2 = []
# for i in numbers:
#     if i % 2 == 0:
#         num1.append(i)
#     else:
#         num2.append(i)
# del numbers
# print(num1)
# print(num2)