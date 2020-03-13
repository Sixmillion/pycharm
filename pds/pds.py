import pandas as pd
import numpy as np
#Series:带索引的一维数组
a=['as','a','good','boy','aha']
b={'name':'jack','age':18,'sex':'boy'}
pd0=pd.Series(a,index=list("abcde"))
# print(pd0.index,pd0.values)
# print(pd0[['a','c','d']])

#Dtaframe:二维数组
df1=pd.read_csv('./dogNames2.csv')
# print(type(pd1))
df2=pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
# print(pd2.sort_values(by=['x','z'],ascending=False))
# print(df2.iloc[:,:2])
# # print(df2[df2>6])#false用nan代替
# print(df1[(df1['Row_Labels'].str.len()>4)&(df1['Count_AnimalName']>700)])
df3=df2[df2>6]
print(df3)
# print(df3.dropna(axis=1,how='any'))#每一列只要存在nan就删除该列
print(df3.fillna(df3.mean()))

