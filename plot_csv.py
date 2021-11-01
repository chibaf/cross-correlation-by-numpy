import numpy as np
import sys
import matplotlib.pyplot as plt

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
mt=m.T

if len(mt)==2:
  v1=mt[0];v2=mt[1];
  x=range(len(v1)) #plot array
  plt.plot(x,v1)
  plt.plot(x,v2)
  plt.show()
else:
  x=range(len(mt)) #plot array
  plt.plot(x,mt)
  plt.show()

exit()
