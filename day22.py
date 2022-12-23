import numpy as np

with open("./day22/input.txt", 'r') as file:
    data = file.read()
N = 50

map_, path = data.split("\n\n")
map2D = map_.split("\n")

map2D = np.empty((1000, 1000), dtype=str)
map2D.fill(" ")
j_max = 0
for i, line in enumerate(map_.split("\n")):
    for j, c in enumerate(line):
        map2D[i, j] = c
        if j > j_max:
            j_max = j
m, n = i+1, j_max+1
map2D = map2D[:m, :n]

i, j = 0, 0
for j in range(n):
    if map2D[i, j] == ".":
        break
directions = {0: (0, 1),  # right
              1: (1, 0),  # down
              2: (0, -1),  # left
              3: (-1, 0)}  # up
facing = 0


def walk(i, j, steps, di, dj):
    # i, j, steps, di, dj = 0, 8, 10, 0, 1
    # i, j, steps, di, dj = 5, 10, 5, 0, 1
    for _ in range(steps):
        i2, j2 = (i+di) % m, (j+dj) % n
        while map2D[i2, j2] == " ":
            i2, j2 = (i2+di) % m, (j2+dj) % n
        if map2D[i2, j2] == ".":
            i, j = i2, j2
        elif map2D[i2, j2] == "#":
            break
    print("walked "+str(_)+" steps to "+map2D[i, j]+" at", i, j)
    return i, j


# walk the path
steps = ""
for digit in path:
    if digit == "L":
        print(steps, "L, dir=", facing)
        i, j = walk(i, j, int(steps), *directions[facing])
        steps = ""
        facing = (facing-1) % 4
    elif digit == "R":
        print(steps, "R, dir=", facing)
        i, j = walk(i, j, int(steps), *directions[facing])
        steps = ""
        facing = (facing+1) % 4
    else:
        steps += digit
i, j = walk(i, j, int(steps), *directions[facing])
steps = ""
r, c = (i+1), (j+1)
print(r, c, facing)
pw = 1000*r+4*c+facing
print(pw)


# task b
def turn_down(cube):
    return np.rot90(cube, k=1, axes=(0, 2))


def turn_up(cube):
    return np.rot90(cube, k=1, axes=(2, 0))


def turn_left(cube):
    return np.rot90(cube, k=1, axes=(2, 1))


def turn_right(cube):
    return np.rot90(cube, k=1, axes=(1, 2))


def make3D(map2D):
    cube = np.empty((N+2, N+2, N+2), dtype=map2D.dtype)
    i, j = 3, 0
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_down(cube)
    i, j = 2, 0
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_left(cube)
    i, j = 2, 1
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_down(cube)
    i, j = 1, 1
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_down(cube)
    i, j = 0, 1
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_left(cube)
    i, j = 0, 2
    cube[1:-1, 1:-1, 0] = map2D[i*N:(i+1)*N, j*N:(j+1)*N]
    cube = turn_right(cube)
    return cube


r, c = np.mgrid[0:4*N, 0:4*N]
cube = make3D(map2D)
rows = make3D(r)
cols = make3D(c)


def walk3D(i, j, steps, di, dj, cube, r, c):
    for _ in range(steps):
        i2, j2 = (i+di), (j+dj)
        print(i2, j2)
        cube2 = cube.copy()
        r2 = r.copy()
        c2 = c.copy()
        if i2 < 1:
            cube2 = turn_down(cube)
            r2 = turn_down(r)
            c2 = turn_down(c)
            i2 = N
        elif i2 > N:
            cube2 = turn_up(cube)
            r2 = turn_up(r)
            c2 = turn_up(c)
            i2 = 1
        if j2 < 1:
            cube2 = turn_right(cube)
            r2 = turn_right(r)
            c2 = turn_right(c)
            j2 = N
        elif j2 > N:
            cube2 = turn_left(cube)
            r2 = turn_left(r2)
            c2 = turn_left(c2)
            j2 = 1
        if cube2[i2, j2, 0] == ".":
            i, j = i2, j2
            cube = cube2.copy()
            r = r2.copy()
            c = c2.copy()
        elif cube2[i2, j2, 0] == "#":
            break  # dont set cube = cube2
    print("walked "+str(_)+" steps to "+cube[i, j, 0]+" at", i, j)
    return i, j, cube, r, c, None


i, j = 1, 1
facing = 0
steps = ""
for digit in path:
    if digit == "L":
        print(steps, "L, dir=", facing)
        i, j, cube, rows, cols, f = walk3D(i, j, int(steps), *directions[facing], cube, rows, cols)
        steps = ""
        facing = (facing-1) % 4
    elif digit == "R":
        print(steps, "R, dir=", facing)
        i, j, cube, rows, cols, f = walk3D(i, j, int(steps), *directions[facing], cube, rows, cols)
        steps = ""
        facing = (facing+1) % 4
    else:
        steps += digit
i, j, cube, rows, cols, f = walk3D(i, j, int(steps), *directions[facing], cube, rows, cols)
steps = ""
r, c = rows[i, j, 0]+1, cols[i, j, 0]+1

side = cube[1:-1, 1:-1, 0]
for k, s in enumerate([side, np.rot90(side, k=1), np.rot90(side, k=2), np.rot90(side, k=3)]):
    for i in range(4):
        for j in range(4):
            if map2D[i*N:(i+1)*N, j*N:(j+1)*N].size > 0:
                if np.all(s == map2D[i*N:(i+1)*N, j*N:(j+1)*N]):
                    f = (facing-k) % 4
pw = 1000*r+4*c+f
print(pw)
# 146, 2, 3 -> 146011 is right :)
