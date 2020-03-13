#格式化的输入和输出
year=2019
event='study'
c=f'i will {event} in {year}'
str='we are {0} champion {1}'.format('the''!')#{}作为占位符
str1='we are the {ch}'.format(ch='champion')
print(str)
#文件操作
with open('test.txt','a+') as file:
    print(file.readline())
file=open('test.txt')
content=file.readlines()#返回行元素的列表
print(content)
file.close()
f=open('workfile','wb+')
f.write(b'0123456789abcdefg')
f.seek(3,0)#0表示从开头，1表示当前位置，2表示从结尾
con=f.read(1)
print(con)
position=f.tell()#告诉当前位置
f.close()
