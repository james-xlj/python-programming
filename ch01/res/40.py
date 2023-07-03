# fruits={'apple','orange','pear'}
# print(fruits)

# final={'阿根廷','克罗地亚','法国','摩洛哥'}
# print(final)
# s={'a','q','w','a','h','g'}
# print(s)
# a='123321'
# s1=set(a)
# print(s1)

# s2=set()
# print(s2)
# print(len(s2))

d1={'first':1,'second':2,'third':3,'first':2}
print(d1)

# 笔记：
#字符串string&元组tuple：  1.元组没有重复元素    
#2.元组中如果只有一个元素，那么这个元素的后边需要加逗号    
#3.元组&字符串中的元素不可以被修改    4.元组使用小括号    
#5.字符串split函数   a.split(分割符,次数(可填可不填))


#集合set：    1.创建空集合：变量名=set()      
#2.集合是无序的不重复元素序列    
#3.集合增加元素的两种方式：一：add   二：update
#4.集合的删除指令：一：remove   二：discard   三：pop     
#(注意：remove指令删除元素时如果没有这个元素，程序会报错,
#而discard指令删除元素时如果没有这个元素，程序不会报错) 
#pop指令：pop指令删除第一个元素       
#注：3，4语法：集合变量名.操作(...)    
#5.集合的操作：并：|   交：&   差：-    
#a = {1,2,3}
#b = {3,4,5}
#print("并集：",a|b) 
#print("交集：",a&b)
#print("差集(a-b):",a-b)
#print("差集(b-a):",b-a)
#{1，2，3，4，5}   {3}   {1，2}   {4，5}
#7.如果打印一个集合，那么顺序会被打乱


#字典dict：    
#1.字典以键值对的方式储存元素    2.字典是无序的    
# 3.字典的获取方法：一.key值 
#                  for key in a.keys(): 
                   
#二.value值                  三.key&value值(items)
#for value in a.values():    for key,value in a.items():

#4.查找元素是否在字典中: a = {"one":1,"two":2,"three":3,"four":4}
#                        c = "one"
#                        if c in a:
#                            print("yes")   #yes
#5.字典与集合使用大括号


#Turtle绘图：1.简写   forward[表情]fd;left[表情]lt;right[表情]rt   
#2.Turtle绘图如果不设置画笔，则将pen替换为turtle


#列表list：    1.列表是使用中括号“[]”整理的一个序列   
#2.列表有增，删，改与查4个操作 
