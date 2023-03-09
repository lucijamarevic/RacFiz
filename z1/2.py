import random as rnd

## gemeriramo nasumisni broj i onda s obzirom na to u kojem je podintervalu
## intervala [0,1] stvaramo njegov novi polozaj

def setac(N):
    xi, yi = 0, 0   # krece iz ishodista
    x, y = [xi], [yi]
    for i in range(N):
        tempx, tempy = xi, yi
        a = rnd.uniform(0,1)
        if a <= 0.1:
            xi = 0.05*tempx
            yi = 0.6*tempy
        elif a > 0.1 and a y <= 0.2:
            xi = 0.05*tempx
            yi = -0.5*tempy + 1
        elif a > 0.2 and a <= 0.4:
            xi = 0.46*tempx - 0.15*tempy
            yi = 0.39*tempx + 0.38*tempy + 0.6
        elif a > 0.4 and a <= 0.6:
            xi = 0.47*tempx - 0.15*tempy
            yi = 0.17*tempy + 0.42*tempy + 1.1
        elif a > 0.6 and a <= 0.8:
            xi = 0.43*tempx + 0.28*tempy
            yi = -0.25*tempx + 0.45*tempy + 1.0
        elif a > 0.8 and a <= 1:
            xi = 0.42*tempx + 0.26*tempy
            yi = -0.35*tempx + 0.31*tempy + 0.7
        else:
            raise ValueError("Nešto je pošlo po krivu")
        x.append(xi)
        y.append(yi)
            