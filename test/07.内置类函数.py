#_call_:提供给对象可以被执行的能力，就像函数那样，而本质上，函数就是对象，函数就是一个拥有__call__方法的对象
#我们可以使用__call__方法来实现实例化对象作为装饰器：
class checker(object):
    def __init__(self,checknum=2):
        self.checknum=checknum
    def __call__(self, func):
        self.func=func
        def check(*args):
            if len(args)!=self.checknum:
                return None
            return func(*args)
        return check
@checker(2)
def calculater(a,b):
    print(a+b)

# iter、next
# 这2个方法用于将一个对象模拟成序列
class obj(object):
    def __init__(self,max_num):
        self.max_num=max_num
        self.counter=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter<self.max_num:
            self.counter+=1
            return self.counter
        else:
            raise StopIteration('迭代停止')
    def __str__(self):
        return self.counter

# hasattr(obj, name)：检查 obj 对象是否包含名为 name 的属性或方法。
# getattr(object, name[, default])：获取 object 对象中名为 name 的属性的属性值。
# setattr(obj, name, value，/)：将obj 对象的 name 属性设为 value。

class StudentManager(object):

    dict={}

    def __getitem__(self, item):
        return self.dict[item]
    def __setitem__(self, key, value):
        self.dict[key]=value




if __name__ == '__main__':
    calculater(12,13)
    obj=obj(10)
    for i in obj:
        print(i)
