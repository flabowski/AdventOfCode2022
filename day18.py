# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 17:11:37 2022

@author: flori
"""
import numpy as np
points = np.genfromtxt("./day18/input.txt", delimiter=",", dtype=np.int32)
print(points.min(axis=0), points.max(axis=0))
N = points.max()+1 + 2  # ghost points
grid = np.zeros((N, N, N))
grid[points[:, 0]+1, points[:, 1]+1, points[:, 2]+1] = 1


# find air pockets
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1000000)
# calls = np.zeros((N, N, N))
# print("max_calls:", N*N*N*6)
# # -1: air
# # 0: water
# # 1: lava
# grid[grid==0] = -1  # air
# def mark_water(i, j, k):
#     if 0<=i<N and 0<=j<N and 0<=k<N:
#         calls[i, j, k] += 1
#         if grid[i, j, k] == -1:
#             grid[i, j, k] = 0
#             mark_water(i-1, j, k)
#             mark_water(i+1, j, k)
#             mark_water(i, j-1, k)
#             mark_water(i, j+1, k)
#             mark_water(i, j, k-1)
#             mark_water(i, j, k+1)
# mark_water(0, 0, 0)


# -1: air
# 0: water
# 1: lava
grid[grid==0] = -1  # air
def flood(i, j, k):
    if 0<=i<N and 0<=j<N and 0<=k<N:
        if grid[i, j, k] == -1:
            grid[i, j, k] = 0
    return

grid[0, :, :] = grid[-1, :, :] = 0
grid[:, 0, :] = grid[:, -1, :] = 0
grid[:, :, 0] = grid[:, :, -1] = 0
for _ in range(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if grid[i, j, k] == 0:
                    flood(i-1, j, k)
                    flood(i+1, j, k)
                    flood(i, j-1, k)
                    flood(i, j+1, k)
                    flood(i, j, k-1)
                    flood(i, j, k+1)

surface_sides = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        for k in range(1, N-1):
            if grid[i, j, k] == 1.0:

                if grid[i-1, j, k] == 0:
                    surface_sides += 1
                if grid[i+1, j, k] == 0:
                    surface_sides += 1

                if grid[i, j-1, k] == 0:
                    surface_sides += 1
                if grid[i, j+1, k] == 0:
                    surface_sides += 1

                if grid[i, j, k-1] == 0:
                    surface_sides += 1
                if grid[i, j, k+1] == 0:
                    surface_sides += 1
print(surface_sides)
