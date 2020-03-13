#捕获异常
try:
    a=10/0
    open('word','r')
except (IOError,ZeroDivisionError) as result:
    print("IOError and ZeroDivisionError")
    print("异常信息：",result)
else:
    print("nothing is error")
#try...finally：无论有无异常都要执行finally的语句
#可嵌套，可用于函数中，异常和i层级传递
#自定义异常
class strIsToShort(Exception):
    def __init__(self,len,atleast):
        self.len=len
        self.atleast=atleast
    def main(self):
        try:
            s = input("请输入字符串")
            if len(s) < 3:
                raise strIsToShort(len(s), 3)
        except strIsToShort as result:
            print('你输入的长度是：%d,至少是：%d'%(len(s),3))
        else:
            print("输入正确")
#异常中的异常
