import numpy as np
map0 = np.genfromtxt("./day23/input.txt", delimiter=1, dtype=str, comments="%")

padding = np.zeros_like(map0)
padding.fill(".")
mapr = np.c_[padding, map0, padding]
padding = np.c_[padding, padding, padding]
map_ = np.r_[padding, mapr, padding]
    
def printmap(map_, ie=None, je=None):
    # i, j = ie, je = [7, 11]
    for i, row in enumerate(map_):
        for j, elem in enumerate(row):
            if i == ie and j == je:
                print("E", end="")
            else:
                print(elem, end="")
        print()

elves = np.empty((0, 2), dtype=np.int32)
for i, row in enumerate(map_):
    for j, elem in enumerate(row):
        if elem == "#":
            elves = np.r_[elves, [[i, j]]]


def check(i, j, direction):
    if direction=="n" and np.all(map_[i-1, j-1:j+2] != "#"):  # n
        return i-1, j
    elif direction=="s" and np.all(map_[i+1, j-1:j+2] != "#"):  # s
        return i+1, j
    elif direction=="w" and np.all(map_[i-1:i+2, j-1] != "#"):  # w
        return i, j-1
    elif direction=="e" and np.all(map_[i-1:i+2, j+1] != "#"):  # e
        return i, j+1
    else:
        return False


def propose(i, j, order):
    if (map_[i-1:i+2, j-1:j+2] == "#").sum() == 1:
        return i, j  
    for direction in order:
        res = check(i, j, direction)
        if res:
            return res
    return i, j


positions = np.zeros((len(elves), 2))
order = ["n", "s", "w", "e"]
n_moves = 1
r = 0
# for r in range(10):
while n_moves > 0:
    r += 1
    for i, elve in enumerate(elves):
        positions[i] = propose(elve[0], elve[1], order)
    d = order.pop(0)
    order.append(d)
    
    n_moves = 0
    for i, elve in enumerate(elves):
        is_proposed = (positions[:, 0] == positions[i, 0]) & (positions[:, 1] == positions[i, 1])
        assert np.sum(is_proposed) != 0, "oops"
        if np.sum(is_proposed) == 1:
            if elves[i, 0] == positions[i, 0] and elves[i, 1] == positions[i, 1]:
                pass
            else:
                elves[i] = positions[i]
                n_moves += 1
        else:
            positions[is_proposed] = elves[is_proposed]
    map_.fill(".")   
    for i, elve in enumerate(elves):
        map_[elve[0], elve[1]] = "#"
    print("== End of Round {:.0f} ==".format(r+1))
    # printmap(map_)
    print(n_moves)
# l = map_ == "."
# rs, re = 0, map_.shape[0]-1
# cs, ce = 0, map_.shape[1]-1

# while np.all(l[rs, :]):
#     rs += 1
# while np.all(l[re, :]):
#     re -= 1
# while np.all(l[:, cs]):
#     cs += 1
# while np.all(l[:, ce]):
#     ce -= 1
# section = map_[rs:re+1, cs:ce+1]
# printmap(section)
# print((section == ".").sum())
print(r)
    
