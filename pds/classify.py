import pandas as pd
import numpy as np
file_path='./IMDB-Movie-Data.csv'
df=pd.read_csv(file_path)
print(df.columns)
#统计演员的数量
temp=df['Actors'].str.split(', ')
acts=[j for i in temp for j in i]
# print(len(set(acts)))
#统计各个类别电影的数量
temp1=df['Genre'].str.split(',')
Genre=[j for i in temp1 for j in i]
Genre_list=[i for i in set(Genre)]
clf=pd.DataFrame(np.zeros((1000,len(Genre_list))),columns=Genre_list)
for i in range(1000):
    clf.loc[i,temp1[i]]=1.0
print([clf[i].sum() for i in Genre_list])