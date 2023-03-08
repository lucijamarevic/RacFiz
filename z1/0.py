import numpy.random as rnd
import matplotlib.pyplot as plt
from math import sqrt

N = [i*1000 for i in range(1,int(1e7/1000)+1)]

def m3(n):
    momenti = []
    suma = 0
    #x = rnd.uniform(-5,5,size=n)
    x = rnd.rand(n)
    for i in range(1,n+1):
        suma += x[i-1]**3
        if (i%1000 == 0):
            e = abs(suma/i - 0.25)
            momenti.append(e*sqrt(i))
    return momenti

#m3(10)
momenti = m3(int(1e7))
plt.scatter(N,momenti, s = 5, c = "orange", edgecolors="face")
#plt.xticks(N)#, labels=["1","2","3","4","5","6","7","8","9","10"])
plt.xlabel("N/10^7")
plt.ylabel("N^1/2 |M(3) - 0.25|")
plt.show()