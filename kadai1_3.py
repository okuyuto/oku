# -*- coding: utf-8 -*-

d_student = {"B4":86, "D3":1, "B3":91, "D2":0, "M2":17, "B2":102, "D1":1, "M1":21, "B1":110}
d = 0
m = 0
b = 0

for key, value in zip(d_student.keys(), d_student.values()):
    if 'D' in key:
        d += value
    elif 'M' in key:
        m += value
    elif 'B' in key:
        b += value

print("D: ", d, "人", sep="")
print("M: ", m, "人", sep="")
print("B: ", b, "人", sep="")