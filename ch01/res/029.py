a=[12,34,5.2,67,42,12,55,12]
b=['a','ab','b','bc']
print('列表a的最大值是%d'%(max(a)))
print('列表a的最小值是%.1f'%(min(a)))
a.sort(reverse=True)
print(a)
print('列表b中的最小值是%s'%(min(b)))

