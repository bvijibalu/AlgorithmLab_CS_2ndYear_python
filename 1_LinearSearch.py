import time
import matplotlib.pyplot as plt
import random

def linearSearch(arr,x):
  for i in range(len(arr)):
    if x==arr[i]:
      return i
  return -1

nValues=[10,100,1000,10000,100000,1000000]
timeValues=[]
for n in nValues:
  arr=[random.randint(0,n) for i in range(n)]
  x=random.randint(0,n)
  startTime=time.time()
  linearSearch(arr,x)
  endTime=time.time()
  timeValues.append(endTime-startTime);

plt.plot(nValues,timeValues)
plt.title("Linear Search")
plt.xlabel("Number of elements")
plt.ylabel("Time taken(seconds)")
plt.show()