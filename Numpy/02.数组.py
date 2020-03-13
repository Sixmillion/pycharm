import  numpy as np
from matplotlib import pyplot as plt
import matplotlib

a=sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
axis_x=np.arange(0,3*np.pi,0.1)
axis_y=np.sin(axis_x)
plt.rcParams['font.family']=['STFangsong']
plt.xlabel('x轴')
plt.ylabel('y轴')
plt.figure(figsize=(20,8),dpi=80)
plt.plot(axis_x,axis_y)
plt.show()