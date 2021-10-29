import numpy as np
import sys
import matplotlib.pyplot as plt

def find_index(c):  # find index of maximum value
  mc=np.amax(c)
  for i in range(len(c)):
    if c[i]==mc:
      im=i
      break
  return im

m=np.loadtxt(sys.argv[1],delimiter=',')  # convert a csv file to a matrix from file sys.argv[1]
mt=m.T #transpose matrix

#computing cross-correlation by fft
v1=mt[1][12500:22500];v2=mt[2][12500:22500]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2)) 
corr=np.real(np.fft.ifft(np.fft.fft(v1)*np.conjugate(np.fft.fft(v2))))*c
#find max
print(np.amax(corr))
print(find_index(corr))

print(len(mt[1]))
x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()

exit()
