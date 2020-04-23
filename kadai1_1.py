# -*- coding: utf-8 -*-

def ave(x):
    a = 0
    for i in range(len(x)):
        a += x[i]
    return a / len(x)


M = [[50, 50, 80, 70, 90],
    [50, 70, 60, 90, 100],
    [90, 80, 90, 90, 80],
    [0, 40, 60, 20, 70],
    [60, 80, 90, 80, 90]]

Mave = [ave(M[0]), ave(M[1]), ave(M[2]), ave(M[3]), ave(M[4])]
Mave = sorted(Mave)
Mave = Mave[::-1]
for i in range(5):
    print(i+1, "位:", Mave[i], sep="")



