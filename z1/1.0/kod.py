from numpy import append
import numpy.random as rnd
import matplotlib.pyplot as plt

N = [i*100 for i in range(1,int(1e7/100)+1)]

def m3(n):
    momenti = []
    suma = 0
    x = rnd.rand(n)
    for i in range(1,n+1):
        #print(x[i-1]**3) 
        suma += x[i-1]**3
        if (i%100 == 0):
            momenti.append(suma/i)
        #print(suma)
        #print(suma/i)
    return momenti

#m3(10)
momenti = m3(int(1e7))
plt.scatter(N,momenti)
plt.show()