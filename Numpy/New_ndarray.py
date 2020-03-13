import numpy as np
#数组的创建
a=np.array([5,3,8,6])
b=np.arange(0,20,4)
c=np.arange(20).reshape(4,5)
d=np.empty((2,3),int)
f=np.random.random((2,3))
complex=np.array([[3.+4.j,6.-2.j,1.+5.j],[8.+8.j,5.-6.j,4.+4.j]])
# print(f)
#数组的属性
dim=c.ndim
type=c.dtype
size=c.size
shape=c.shape
# print(dim,type,shape,size)
#数组的基本操作
add_c=np.ones_like(c)
add=c+add_c
mul=c*add_c
mitrix_mul=c.dot(add_c.T)
add_c*=3
sum=f.sum(axis=0)#按0轴比较
max=f.max(axis=1)
min=f.min(axis=1)
# print(sum,max,min)
#通用函数
num=np.linspace(0,np.pi,6)
sin=np.sin(num)
exp=np.exp(num)
log=np.log2(np.array([2,2**2,2**3]))
abs=np.absolute(np.negative(np.arange(3)))
H=np.conj(complex.T)
# print(H)
#索引、切片和迭代
onedim=np.array([0,1,2,3,4,5])
twodim=np.arange(16).reshape(4,4)
threedim=np.arange(27).reshape(3,3,3)
one_a=onedim[2]
one_list=onedim[2:5]
one_list2=onedim[::2]
#多维的数组每个轴可以有一个索引。这些索引以逗号​​分隔的元组给出：
two_a=twodim[2,3]
two_list=twodim[3,::2]#选取第三行，隔1位选取
three_a=threedim[2,1,0]
three_list=threedim[1,:,1]
# print(np.floor(3.6))
#改变数组形状，拷贝与视图
rand=np.floor(10*np.random.random((3,4)))
rand_rav=rand.ravel()
rand_reshape=rand.reshape(2,6)#视图
rand.resize(6,2)#直接修改
arr=np.arange(5)
view_a=arr.view()
copy_a=arr.copy()
#数组的拆分和组合
#concatenate:拼接轴元素数可不同，其他轴元素数必须一致
arr1=np.array([[1,2,3],
                [3,4,5]])
arr2=np.array([[5,6,6]])
new_arr0=np.concatenate((arr1,arr2),axis=0)
new_arr1=np.concatenate((arr1.T,arr2.T),axis=1)
#stack:增加维度，直接罗列
arr3=np.array([1,2,3])
arr4=np.array([4,5,6])
new_stack0=np.stack([arr3,arr4],axis=0)
new_stack1=np.stack([arr3,arr4],axis=1)
#vstack:vertical:在高于两维是等价与concatenate的0轴，同row stack
#一维时有所不同
#hsatck:horizontal:在高于两维时等价与contcatenate的1轴，同column stack
#一维是等价与concatenate的0轴
#column_stack 将一维数组作为列堆叠
#row_stack 将一维数组作为行堆叠
#hsplit(arr,n)将数组水平切分为n个数组
#vsplit(arr,n)将数组垂直切分为n个数组

#花式索引
#被索引数组为一维时
index1=onedim[[0,1,3]]
index_arr1=np.array([[0,1],[2,3]])
index2=onedim[index_arr1]#多维数组索引一维数组为多维数组
#被索引数组是多维时
index3=twodim[:,[1,3]]#对角元素
index_arr2=np.array([[2,0,1,3],[3,1,0,0]])
index_arr3=np.array([[[2,0,1,3],[2,0,1,3]],[[3,1,0,0],[3,1,0,0]]])
i=np.array([[2,0,1,3],[2,0,1,3]])
j=np.array([[3,1,0,0],[3,1,0,0]])
index4=twodim[index_arr2]
index5=twodim[index_arr3]
index6=twodim[i,j]
#布尔索引

print(index3)

