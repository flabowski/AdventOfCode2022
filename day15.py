# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 19:44:23 2022

@author: flori
"""
import numpy as np

with open("./day15/input.txt", 'r') as file:
    data = file.read()

def distance(a, b):
    dx, dy = abs(a[0]-b[0]), abs(a[1]-b[1])
    return dx+dy


s = []
b = []
d = []
x1, x2 = 0, 1
y1, y2 = 0, 1
for i, line in enumerate(data.split("\n")):
    # Sensor at x=1891025, y=3796582: closest beacon is at x=3369445, y=3597264
    p1, p2 = line.split(": closest beacon is at x=")
    x, y = p1.replace("Sensor at x=", "").split(", y=")
    s.append([int(x), int(y)])
    x, y = p2.split(", y=")
    b.append([int(x), int(y)])
    d.append(distance(s[i], b[i]))
    x1 = min(x1, s[i][0]-d[i])
    x2 = max(x2, s[i][0]+d[i])
    y1 = min(y1, s[i][1]-d[i])
    y2 = max(y2, s[i][1]+d[i])
print(x1, x2)
print(y1, y2)

x = np.arange(x1, x2+1)
row = np.zeros_like(x)
y = 2000000
# y = 10
for i, sensor in enumerate(s):
    l = np.abs(x-s[i][0]) <= (d[i]-abs(s[i][1]-y))
    row[l] = 1
print(x)
print(row.sum()-1)


def check(p):
    # print("p =", p)
    c1 = True
    for i, sensor in enumerate(s):
        c1 = c1 and distance(p, sensor) > d[i]
    c2 = 0 <= p[0] <= 4000000
    c3 = 0 <= p[1] <= 4000000
    if c1 and c2 and c3:
        print(p, "meets all conditions")
        tf = p[0] * 4000000 + p[1]
        print(tf)
    
for i, sensor in enumerate(s):
    x, y = sensor[0]-d[i]-1, sensor[1]
    while x <= sensor[0]:
        check([x, y])
        x += 1
        y += 1
    x, y = sensor[0]-d[i]-1, sensor[1]
    while x <= sensor[0]:
        check([x, y])
        x += 1
        y -= 1

    x, y = sensor[0]+d[i]-1, sensor[1]
    while x >= sensor[0]:
        check([x, y])
        x -= 1
        y += 1
    x, y = sensor[0]+d[i]-1, sensor[1]
    while x >= sensor[0]:
        check([x, y])
        x -= 1
        y -= 1
    
    
    # check([sensor[0]+d[i], sensor[1]])
    # check([sensor[0]-d[i], sensor[1]])
    # check([sensor[0], sensor[1]+d[i]])
    # check([sensor[0], sensor[1]-d[i]])


# # for x in range(4000000):
# x = np.arange(4000000)
# row = np.zeros_like(x)
# for y in range(4000000):
#     for i, sensor in enumerate(s):
        
#         l = np.abs(x-s[i][0]) <= (d[i]-abs(s[i][1]-y))
#         row[l] = 1
#     # print(x)
#     if row.sum()<4000000:
#         print(x[row!=1], y, row.sum())
# # x = y = np.arange(4000000, dtype=np.int32)
# # im = np.zeros((4000000, 4000000), dtype=np.int32)
# # for i, sensor in enumerate(s):
# #     l = 