import matplotlib.pyplot as plt
import numpy as np
import statistics as sta

ecg = np.loadtxt("ECG record.txt")
y = ecg[10:2500]
ln = len(y)
x = np.arange(0, ln, 1)
plt.plot(x, y)
#finding the R index from ECG database
maxim = np.max(y)
t = 0.6 * maxim
RX = np.zeros(ln)
RY = np.zeros(ln)
for n in range(ln - 1):
  if y[n] >= t:
    if y[n] > y[n + 1] and y[n] > y[n - 1]:
      RX[n] = n
      RY[n] = y[n]
RX = [i for i in RX if i != 0]
RY = [j for j in RY if j != 0]
print("The index of R :", RX)
#R-R interval calculation
lngth = len(RX)
I = np.zeros(lngth)
legn = lngth - 1
for i in range(legn):
  I[i] = RX[i + 1] - RX[i]
I = I[0:18]
print("\nThe R-R interval:", I)
#finding mean to find the deviation in R-R interval
M = sta.mean(I)  #finding using in-build function
N = len(I)
su = sum(I)
mean = su / N  #finding using logic
print("\nThe mean of interval:",M)
#finding standard deviation
d = np.zeros(N)
for l in range(N):
  d[l] = (I[l] - mean)**2
  s = sum(d)
de = s / N
sd = np.sqrt(de)  #finding using logic
sdn = sta.stdev(I)  #finding using in-build function
print("\nThe standard deviation of interval:",sdn)
