def fib(n):
    a,b=0,1
    while(a<n):
        print(a," ",end='')
        a,b=b,a+b
fib(20)
#定义缺省参数
def info(age,name='levry'):#定义缺省参数
    print(name+' is '+age)
info('21')
#定义不定长参数
def fun(a,b,*args,**kvargs):#*args：列表，**kvargs：字典
    print(a+b)
    print(args)
    for k,v in kvargs.items():
        print(k+"->"+v)
list=['x','y','z']
dict={'m':6,'n':8}
fun(33,54,36,85,m="sas",s="sassdd")
fun(3,9,list,dict)
