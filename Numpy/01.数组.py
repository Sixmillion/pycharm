import numpy as np
#ndarray:维度(dim)<=>轴(axes)<->秩
#shape:矩阵形状 size:元素总个数
#dtype:指定数组元素类型
b=np.array([[1,2,3],
            [1,5,3],
            [4,5,6]],dtype=int)
zeros=np.zeros((3,3))
ones=np.ones((3,3))
one_like=np.ones_like(b)
empty=np.empty((3,3))
ar=np.arange(10,30,5)
x=np.arange(9).reshape(3,3)
y=np.array([[1,0,0],
           [0,1,0],
           [0,0,1]])
dot=x.dot(y)
#不同类型数组运算采用向上(更精确)转换
arr=np.arange(12).reshape(3,4)
arr.max()
arr.min()
print(arr.sum(axis=0))
#通用函数(逐个位置计算)
tem=np.arange(3)
# print(tem[::-1])#顺序反传
# for i in tem:
#     print(i**(1/3))
tem1=np.arange(25).reshape(5,5)
# for i in tem1.flat:
#     print(i)
#修改数组的形状，以视图的形式返回
t=np.floor(10*np.random.random((2,3)))
p=np.floor(10*np.random.random((2,3)))
# t.reshape(1,6)
# t.resize()#修改原数组
# t.T
# print(t.ravel())#铺平
#数组的堆叠
np.vstack((t,p))#0轴
np.row_stack((t,p))
# print(np.c_[[1,2,3],[4,5,6]])
np.hstack((t,p))#1轴
np.column_stack((t,p))#作为列向量堆叠
# print(np.r_[[1,2,3],[4,5,6]])
#数组的切分
# r=np.arange(6).reshape(2,3)
# print(np.vsplit(r,2))#0轴
# print(np.hsplit(r,3))#1轴
# print(np.array_split(r,2,0))#指定轴
# print(np.all([[True,False],[True,True]], axis=0))#and
c=np.arange(16).reshape(4,4)
e=c.view()
d=c.copy()
# print(d is c,e.base is c)
#花式索引
#一维索引
# print(c[1,2])
# print(c[[2,3],[1,2]])#行索引和列索引
# rows = np.array([[0,0],[3,3]])#0轴的0行和3行分别由两个元素
# cols = np.array([[0,3],[0,3]])#这4个元素分别是0，2列的
# print(c[rows,cols])
a = np.arange(12).reshape(3,4)
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
# print(a[b1,b2])
aa = np.array([2,3,4,5])
bb = np.array([8,5,4])
cc = np.array([5,4,6,8,3])
# ax,bx,cx = np.ix_(aa,bb,cc)
# print(np.shape(ax))
# print(np.shape(bx))
# print(np.shape(cx))
aa.itemset(3,100)#在指定位置插入值
# print(bb.tostring())#转化为字节字符串
# print(bb.tolist())
cc.fill(0)#方法：无返回值
bb.flat=1#数组的迭代器，可索引
cf=c.flatten()#将多维数组展开
zl=np.zeros_like(c)
np.argmax(c,axis=0)
com=np.arange(12).reshape(((3,4)))
g1=np.generic()
print(g1)
