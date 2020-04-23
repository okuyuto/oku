# -*- coding: utf-8 -*-

def ave(x):
    a = 0
    for i in range(len(x)):
        a += x[i]
    return a / len(x)
    

def cov(x, y):
    dev = []
    xave = ave(x)
    yave = ave(y)
    for x, y in zip(x, y):
        dev.append((x - xave) * (y - yave))
    return ave(dev)
        

d1 = [50, 50, 80, 70, 90]
d2 = [50, 70, 60, 90, 100]

print(cov(d1, d2))