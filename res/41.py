# a=['a','b','c','d','f','d','c','a']
# a1=set(a)
# print(a1)

# word={'a','b','c'}
# word.add('d')
# print(word)

# word1={'a','b','c'}
# word1.update('d','e','f')
# word1.update('def')
# print(word1)

# word={'a','b','c'}
# word.update('123')
# print(word)

# a={1,2,3,4,5,2,2}
# a.remove(5)
# a.remove(0)
# a.remove(2)
# print(a)

# word={'a','b','c','d'}
# word.discard('b')
# word.discard('e')
# print(word)

# word1={'a','b','c','d'}
# print(word.pop())
# print(word1)

# word={'a','b','c','d'}
# print('a' in word)  #True
# print('e' in word)  #False

# s1={'a','b','c','d'}
# s2={'c','d','e','f'}
# print(s1&s2)
# print(s1|s2)
# print(s2-s1)
# print(s1-s2)

# import random
# a=set()
# for i in range(5):
#     b=random.randint(1,20)
#     a.add(b)
# print(a)
# c={11,2,13,15,16}
# print(a&c)
# print(a-c)
# print(c-a)




a={'李华','王力','张伦'}
b={'李华','赫伦','孙立'}
print(a&b)
print(a|b)
print(a-b)
print(b-a)