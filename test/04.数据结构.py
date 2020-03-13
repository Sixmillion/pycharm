#字符串(不可变元素,'...')
a='py''thon'#可拼接
b='py'+'thon'
#列表(可变元素,[*,*,...])
list=['a']
ex_list=['c','d']
list.append('b')
list.extend(ex_list)
list.insert(len(list),'e')
list.remove('e')
list.pop(3)#删除并返回指定位置的值，缺省为最后一个元素
#list.clear()#清楚列表所有元素
list.index('b')#返回指定元素的索引
list.count('a')#返回出现次数
list.sort()
list.reverse()
print(list)
#lambda表达式（列表推导式:有表达式和for-if子句组成）
squares=[x**2 for x in range(0,6)]
two=[(x,y) for x in range(1,10) for y in range(1,10)
     if x==2*y]
#例：矩阵的转置:将matrix的每个元素的第i个子元素重新作为第j行
matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
transpose=[[row[i] for row in matrix]for i in range(4)]
del list[3]#可以通过索引的方式移除元素或删除列表变量
#元祖（不可变元素，但可包含可变元素，一般用（）表示）
empty=()#0元素元祖
sigle='single',#1元素元祖
#集合（不重复元素组成的无序集合）
a=set('set',1)
b={'set',2}
c=set(list)#可以将列表作为参数
#字典(以关键字作为索引，数字、字符串、不可变序列可以作为关键字）
dict={'key':'value'}
temp=dict['key']#索引
keys=list(dict)
del dict['key']
dict1=dict([('a',4536),('b',4848),('e',236)])#从键值对序列创建
#数据结构循环技巧
#序列
for i,v in enumerate(['da','sdeas','defa']):
    print(i,v)
#字典
for k,v in dict1.item():
    print(k,v)
