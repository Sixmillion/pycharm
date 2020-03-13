import numpy as np
import numpy.linalg as lg
a=np.arange(6).reshape(2,3)
b=np.arange(9).reshape(3,3)
#数组转换
list=a.tolist()
string=a.tostring()#Python字节
byte=a.tobytes()#Python字节
a_float=a.astype(float)
copy=a.copy()
view=a.view()
a.fill(1)
bf=b.flat[0]
#形状操作
ravel=b.ravel()
flatten=b.flatten()
b.resize(1,9)#直接更改数组形状如果可行
#b.reshape((1,9))不能更改已成型的数组
#项目选择
c=np.arange(16).reshape(4,4)
d=np.arange(6)
diagnoal=c.diagonal()
nonzero=d.nonzero()#返回非零元素的索引
take=c.take([1,2],axis=0)#np.take(arr, indices, axis=3)相当于arr[:,:,:,indices,...].
d.put([2,3,4],[1,1,1])#a.flat[n] = values[n]
repeat=c.repeat(2,axis=0)#重复次数和重复轴
choose=np.array([1,3,2,1]).choose(c)#用数组选择对应索引上的元素.
#计算
e=np.random.randint(0,20,(3,4))
max=e.max(axis=0)
argmax=e.argmax(axis=0)
min=e.min(axis=1)
argmin=e.argmin(axis=0)
ptp=e.ptp(axis=0)#计算最大差
clip=e.clip(2,6)#返回区间值的数组
conj=e.conj()#返回复共轭
all=e.all(axis=0)#and
any=e.any(axis=1)#or
sum=e.sum()
mean=e.mean()
std=e.std()
var=e.var(axis=0)
#线性代数
A=np.array([[2,-4,3,7],
            [-8,5,6,4],
            [5,5,1,2],
            [4,5,2,-6]])
B=np.random.randint(3,12,(4,4))
C=np.random.randint(3,12,(3,4))
vector_x=np.random.randint(3,16,3)
vector_y=np.random.randint(1,11,3)
eye=np.eye(3)#单位矩阵
transpose1=A.T
transpose2=A.transpose()
diag=A.diagonal()
dot=np.dot(A,B)
inner=np.inner(vector_x,vector_y)
outer=np.outer(vector_x,vector_y)
det=lg.det(eye)
eig=lg.eig(A)
eigvals=lg.eigvals(A)
trace=A.trace()
rank=lg.matrix_rank(eye)
inv=lg.inv(A)
norm=lg.norm(vector_x,np.inf)#范数：无穷范数
cond=lg.cond(A)#条件数
pinv=lg.pinv(C)#伪逆矩阵
svd=lg.svd(C)#奇异值分解
vector_b=np.random.randint(0,12,4)
solve=lg.solve(A,vector_b)

print(solve)



