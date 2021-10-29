import numpy as np
import sys
import matplotlib.pyplot as plt

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
mt=m.T

v1=mt[0];v2=mt[1];
print("length of array="+str(len(v1)))
x=range(len(v1)) #plot array
plt.plot(x,v1)
plt.show()
x=range(len(v2)) #plot array
plt.plot(x,v2)
plt.show()

exit()