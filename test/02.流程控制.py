#-*-coding utf-8-*-
age=2000
if (age>=1980)and(age<1990):
    print('80后')
elif (age>=1990)and(age<2000):
    print('90后')
else:
    print('00后')
i=1
while i<6:
    j=1
    while j<6:
        print("%d*%d=%d"%(i,j,i*j))
        j+=1
    print("\n")
    i+=1
#for:可以遍历任何序列
word="hello world!"
for i in word :
    print(i)
for i in range(0,10,2):#逆序输出
    print(i)
#break:用于跳出最近的while和for循环
#continue:用于跳过本次循环进入下一次循环
#pass;什么也不做
