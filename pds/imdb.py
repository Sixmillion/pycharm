import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path='./IMDB-Movie-Data.csv'
df=pd.read_csv(file_path)
# mean_rate=df['Rating'].mean()
# dir=df['Director'].tolist()
# num=len(set(dir))
# print(df.columns)
max_rountines=df["Runtime (Minutes)"].max()
min_rountines=df["Runtime (Minutes)"].min()
routines_range=max_rountines-min_rountines
plt.figure(figsize=(20,8),dpi=80)
plt.grid()
x_ticks=[i for i in range(min_rountines,max_rountines)]
plt.hist(df["Runtime (Minutes)"],bins=routines_range//5)
plt.show()
print(routines_range)
