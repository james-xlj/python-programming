# string='去吗，配吗，这褴禄的披风，战吗，战啊，以最卑微的梦'
# s=string.split()
# print(s)

# string='去吗，配吗，这褴禄的披风，战吗，战啊，以最卑微的梦'
# s1=string.split('，')
# print(s1)

# string='去吗，配吗，这褴禄的披风，战吗，战啊，以最卑微的梦'
# s2=string.split('吗')
# print(s2)

# string='去吗，配吗，这褴禄的披风，战吗，战啊，以最卑微的梦'
# s=string.split('，',3)
# print(s)

# a='Hello everyone! My name is Marry.'
# s=a.split()
# for i in a:
#     print(i[0])

# l1=['Hello','everyone!','My','name','is','Marry.']
# s='#'.join(l1)
# print(s)

# s = 'kdk-kldk-dsd'
# s1=s.split('-')
# s2='#'.join(s1)
# print(s2)

# s='i love programming!'
# new=''
# for i in range(len(s)):
#     print(i)
#     if i%3==0:
#         new+=s[i]
# print(new)

# l=['i','love','you','!']
# l='.'.join(l)
# l=l.split('.')
# l=' '.join(l)
# print(l)

# l=['你','好','世','界']
# s=' '.join(l)
# print(s)

#  已知字符串s='5-1-601-602',
# 请将字符串s变为'5/1/601/602'。
s='5-1-601-602'
s1=s.split('-')
s2='/'.join(s1)
print(s2) 
# s='5-1-601-602'
# s1=s.split('-')
# s2='/'.join(s1)
# print(s2) 
