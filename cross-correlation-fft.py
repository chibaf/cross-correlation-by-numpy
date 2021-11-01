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
if len(mt)==2:
  v1=mt[0];v2=mt[1];
else:
  v1=mt[1];v2=mt[2]; 
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2)) 
corr=np.real(np.fft.ifft(np.fft.fft(v1)*np.conjugate(np.fft.fft(v2))))*c

np.savetxt(sys.argv[2],corr,delimiter=',')
#find max
print(np.amax(corr))
print(find_index(corr))

x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()

exit()
