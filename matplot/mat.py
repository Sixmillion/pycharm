import matplotlib.pyplot as plt
import numpy as np
x=[i for i in range(120)]
y=[np.random.randint(25,30) for i in range(120)]
plt.figure(figsize=(20,8),dpi=80)
xticks_1=["10:{}".format(i) for i in range(60)]
xticks_2=["11:{}".format(i) for i in range(60)]
_xticks_=xticks_1+xticks_2
plt.xticks(x[::3],_xticks_[::3],rotation=45)
plt.xlabel('time')
plt.ylabel('tempeture')
plt.title('the range of tempeture')
plt.plot(x,y)
plt.show()