#Director
# 当程序使用“＠函数”（比如函数 A）装饰另一个函数（比如函数 B）时，实际上完成如下两步：
# 1.将被修饰的函数（函数 B）作为参数传给 ＠ 符号引用的函数（函数 A）。
# 2.将函数 B 替换（装饰）成第 1 步的返回值。
# 其实所谓的装饰器，就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。

#计算只含两个参数的和
def checknum(num):
    def decrote(func):
        def check(*args):
            if len(args)!=num:
                print('num of args is illegal')
                return None
            return func
        return check
    return decrote
@checknum(2)
def compute(a,b):
    print(a+b)
#打印符号和求和
def signal(func):
    def print_signal(*args):
        print('===========')
        func(*args)
    return print_signal
@signal
def compute(a,b):
    print(a+b)
#给函数添加参数
def attr(**kwargs):
    def decrote(f):
        for k in kwargs:
            setattr(f,k,kwargs[k])
        return f
    return decrote
# @attr(version=2.0,author='jack')
def excute(p):
    print('========')
    print(getattr(excute,'version',1.0))
    print(getattr(excute,'author','levry'))
    print(p)
#@property
#使调用类中的方法像引用类中的字段属性一样
if __name__ == '__main__':
    compute(12,13)

