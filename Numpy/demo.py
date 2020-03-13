import  numpy as np
from matplotlib import pyplot as plt
import matplotlib
import scipy.integrate as integrate
from scipy import special
f=lambda x:np.sin(x*2+np.pi/4)
# result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
def exception(x,n,t):
    return np.exp(-x*t)/t**n
mitrix=np.array([[2,6,-5,4],[3,-6,4,9],[-2,7,7,3]])
print(np.rank(mitrix))
