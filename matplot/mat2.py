import matplotlib.pyplot as plt
import random
y_1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
x=[x for x in range(len(y_1))]
plt.figure(figsize=(20,8),dpi=80)
plt.grid()
plt.xticks(x,x[::1])
plt.plot(x,y_1,label='boy')
plt.plot(x,y_2,label='girl')
plt.legend()
plt.show()