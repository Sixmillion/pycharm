from matplotlib import pyplot as plt
a = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
b = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]
x_a=[i for i in range(1,32)]
x_b=[i for i in range(51,82)]
plt.figure(figsize=(20,8),dpi=(80))
x_a_labels=['3.{}'.format(i) for i in range(1,32)]
x_b_labels=['10.{}'.format(i) for i in range(1,32)]
plt.xticks((x_a+x_b)[::3],(x_a_labels+x_b_labels)[::3])
plt.grid()
plt.xlabel('Month')
plt.ylabel('tempeture')
plt.scatter(x_a,a,label='March')
plt.scatter(x_b,b,label='October')
plt.legend()
plt.show()