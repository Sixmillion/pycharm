# 定义类
# 1. self表示一个类的实例对象本身。如果用了staticmethod就无视这个self了，
#    就将这个方法当成一个普通的函数使用了。
# 2. cls表是这个类本身。
# 3. 更多： 类先调用__new__方法，返回该类的实例对象，
#    这个实例对象就是__init__方法的第一个参数self，即self是__new__的返回值
class Car(object):
    # 用来实例化类，相当于构造函数
    # cls指的是类本身
    #返回实例可以使父类的实例
    #__new__方法是真正的类构造方法，用于产生实例化对象（空属性）。重写__new__方法可以控制对象的产生过程。
    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)
    #对象创建时就被调用，可传参
    #self指的是new出的实例，类似于this
    # __init__方法是初始化方法，负责对实例化对象进行属性值初始化，
    # 此方法必须返回None，__new__方法必须返回一个对象。重写__init__方法可以控制对象的初始化过程。
    def __init__(self):
        self.color='black'
        self.__price=1000  #在属性名前加__进行私有化
        print("对象被创建")
    #定义私有化属性的set和get方法
    def setPrice(self,price):
        self.__price=price
    def getPrice(self):
        return self.__price
    #对象被删除时执行
    #对象的生命周期到程序运行结束
    def __del__(self):
        print("当前对象被删除")
    #魔法方法
    #类似toString方法，在打印对象时输出特定的字符串和
    #和__repr__方法在print时无差别
    def __str__(self):
        msg='the color is '+self.color+'the price is '+self.getPrice().__str__()
        return msg
    def __repr__(self):
        return 'the color is '+self.color+'the price is '+self.getPrice().__str__()
    def run(self):
        print('car can run')
#继承：
#父类的属性、方法，会被继承
# 一个子类可以继承多个父类
#父类的私有方法和属性不能被集成也不能被访问
class toyCar(Car):
    def play(self):
        print('this is a toy')
toy=toyCar()
car=Car()
car.setPrice(100)
print(car.__repr__())
toy.run()
#重写
#多态
#类属性和实例属性
class Person(object):
    __age=19    #静态类属性（私有）
    name='lili'
    def __init__(self,grade):
        self.number=123321  #动态实例属性
        self.__grade=grade
#类方法和静态方法
class Person(object):
    __country='china'
    @classmethod
    def getConntry(cls):
        return cls.__country
    @classmethod
    def setCountry(cls,name):
        cls.__country=name
    @staticmethod
    def getCou():
        return Person.getConntry()
