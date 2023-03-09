import random as rnd
import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import pi as true_pi
from math import sqrt

def pi_mc(i,r):
    pi, err, r, rk = [], [], {"x": [], "y": []}, {"xk": [], "yk": []}
    k = 0
    for j in range(1,i+1):
        xi = rnd.uniform(0,i)
        yi = rnd.uniform(0,i)
        if (xi**2 + yi**2) <= i**2:
            k+=1
            rk["xk"].append(xi)
            rk["yk"].append(yi)
        else:
            r["x"].append(xi)
            r["y"].append(yi)
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
plt.scatter(data["r"]["x"], data["r"]["y"], s=5)
plt.scatter(data["rk"]["xk"], data["rk"]["yk"], s=5, c="orange")
plt.xlim(0,2e5)
plt.ylim(0,2e5)
plt.show()
