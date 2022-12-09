import numpy as np
with open("./input.txt", 'r') as file:
    data = file.readlines()


# def print_HT(H, T):
#     POS = np.empty((5, 6), dtype=str)
#     POS.fill(".")
#     POS[H[1], H[0]] = "H"
#     POS[T[1], T[0]] = "T"
#     POS[0, 0] = "s"
#     for i in range(5):
#         for j in range(6):
#             print(POS[-1-i, j], end="")
#         print()


def step(P, HT):
    if P == "U":
        HT[1] += 1
    if P == "D":
        HT[1] -= 1
    if P == "R":
        HT[0] += 1
    if P == "L":
        HT[0] -= 1
    return


def hs(dx):
    if dx < 0:
        return -1
    if dx == 0:
        return 0
    if dx > 0:
        return 1


def catch_up(H, T):
    dx, dy = H[0]-T[0], H[1]-T[1]
    if abs(dx) == 2 or abs(dy) == 2:
        T[0] += hs(dx)
        T[1] += hs(dy)
    return


positions = np.zeros((20000, 2))
H = [0, 0]
T = [0, 0]
p = 0
for move in data:
    # print("==", move.strip(), "==")
    direction, steps = move.strip().split()
    for i in range(int(steps)):
        step(direction, H)
        catch_up(H, T)
        # print_HT(H, T)
        positions[p] = T[0], T[1]
        p += 1
positions = positions[:p]
print(np.unique(positions, axis=0).shape)

# task 2
positions *= 0
p = 0
length = 10
Rope = np.zeros((length, 2), dtype=np.int32)
for move in data:
    direction, steps = move.strip().split()
    for i in range(int(steps)):
        step(direction, Rope[0])
        for i in range(length-1):
            catch_up(Rope[i], Rope[i+1])
        positions[p] = Rope[-1, 0], Rope[-1, 1]
        p += 1
positions = positions[:p-1]
print(np.unique(positions, axis=0).shape)
