from matplotlib import pyplot as plt
import numpy as np
a = ["xqjq","dunkerk","spiderman","wolf"]
b_16 = [1574,312,4497,319]
b_15 = [1235,156,2045,168]
b_14 = [2358,399,2358,362]
x=[i for i in range(len(a))]
plt.figure(figsize=(20,8),dpi=80)
plt.bar(x,b_14,width=0.1,label='6.16')
x_labels=['{}'.format(i) for i in a]
plt.xticks([x+0.1 for x in range(len(a))],x_labels)
plt.bar([0.1+x for x in range(len(a))],b_15,width=0.1,label='6.15')
plt.bar([0.2+x for x in range(len(a))],b_16,width=0.1,label='6.14')
plt.legend()
plt.show()