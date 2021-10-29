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
v1=mt[0];v2=mt[1]
c=1.0/(np.linalg.norm(v1)*np.linalg.norm(v2))
corr=np.empty(0)   #make nd.array of length zero
corr=np.append(corr,np.dot(v1,v2)*c)  
d1=v1;
for i in range(len(v1)):
  d2=np.roll(v2,-1)  # shift 1 to the left
  corr=np.append(corr,np.dot(d1,d2)*c) 
#find max
print(np.amax(corr))
print(find_index(corr))

# plot the result
x=range(len(corr)) #plot array
plt.plot(x,corr)
plt.show()

exit()
