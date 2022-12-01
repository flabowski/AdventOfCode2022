# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:38:13 2022

@author: florianma
"""
import numpy as np
src = "./input.txt"
# src =  "./test.txt"

with open(src, 'r') as file:
    inventory = file.readlines()

calories = np.zeros(len(inventory),)

elve = 0
for snack in inventory:
    # print(line, end="")
    if snack == '\n':
        elve += 1
    else:
        calories[elve] += float(snack)

# calories = calories[:elve]
print(calories.max())

calories.sort()
print(calories[-3:].sum())
