import numpy as np

import Numpy.New_ndarray as na
print(na.onedim)
print(na.twodim)
print(na.threedim)
a=np.array([[ 0,  1,  2,  3],
            [ 4,  5,  6,  7],
            [ 8,  9, 10, 11]])
i=np.array( [ [0,1], [1,2] ] )
j=np.array( [ [2,1], [3,3] ] )
for i in range(a.shape[0]):
    print(i)