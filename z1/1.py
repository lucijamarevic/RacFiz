import random as rnd
import matplotlib.pyplot as plt
from scipy.constants import pi as true_pi
from math import sqrt

def pi_mc(i,r):
    pi, err, r, rk = [], [], [], []
    k = 0
    for j in range(1,i+1):
        xi = rnd.uniform(0,i)
        yi = rnd.uniform(0,i)
        if (xi**2 + yi**2) <= i**2:
            k+=1
            rk.append(sqrt(xi**2 + yi**2))
        else:
            r.append(sqrt(xi**2 + yi**2))
        pii = 4*(k/j)
        pi.append(pii)
        erri = abs(pii - true_pi) * sqrt(j)
        err.append(erri)
    dict = {"pi": pi, "err": err, "r": r, "rk": rk}
    return dict

i = [10*i for i in range(20,int(2e5)+1)]
data = pi_mc(int(2e5),1)

plt.plot(i,data["pi"][19:])
#plt.show()

plt.plot(i,data["err"][19:])
#plt.show()

#ode dodat scatter plot za udaljenosti, ovo nije dobro
x1 = np.linspace(0,int(2e5), num = len(data["r"]))
x2 = np.linspace(0,int(2e5), num = len(data["rk"]))
plt.scatter(x1, data["r"], s=5)
plt.scatter(x2, data["rk"], s=5, c="orange")
plt.show()
