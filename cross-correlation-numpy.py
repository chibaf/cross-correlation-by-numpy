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

#computing cross-correlation by shift
v1=mt[1][10000:15000];v2=mt[2][10000:15000]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2))
corr=np.correlate(v2,v1,"same")*c
print(corr.shape[0])
print(corr.shape[1])
#find max
print(np.amax(corr))
print(find_index(corr))

# plot the result
x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()

#computing cross-correlation by fft
v1=mt[1][10000:15000];v2=mt[2][10000:15000]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2)) 
fft_len=13
f1=np.fft.fft(v1)
f2=np.conjugate(np.fft.fft(v2))
ff=f1*f2
corrf=np.real(np.fft.ifft(ff))*c
#find max
print(np.amax(corrf))
print(find_index(corrf))

x=range(len(corrf)) #plot array
plt.plot(x,corrf)
plt.show()

exit()
