#数字（自动识别类型）
#字符串(‘a’，"bb",''' '''将保留tab和enter格式)
print('''\
    abc
    enter''')#r表示忽略转义字符，以\结尾忽略enter
#布尔值
#空值（None）
#关键字
import keyword
print(keyword.kwlist)
#格式化输出
print('小明成绩提升的百分点是%%%f'%((85-72)/72))
#输入
input("请输入")
#运算（/除，//取整，%取余，**幂
#赋值（多赋值）
a,b=1,2
#逻辑运算（与或非：and，or，not）