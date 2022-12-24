import numpy as np

with open("./input.txt", 'r') as file:
    data = file.read()
highest_pt = 0  # task b
cave = np.empty((1000, 1000), dtype=str)
cave.fill(".")

for line in data.split("\n"):
    print(line)
    xy = [elem.split(",") for elem in line.split(" -> ")]
    for i in range(len(xy)-1):
        x1, x2 = sorted([int(xy[i][0]), int(xy[i+1][0])])
        y1, y2 = sorted([int(xy[i][1]), int(xy[i+1][1])])
        cave[y1:y2+1, x1:x2+1] = "#"
#         if y2 > highest_pt:  # task b
#             highest_pt = y2  # task b
# highest_pt = highest_pt + 2  # task b
# cave[highest_pt, :] = "#"  # task b
cave[0, 500] = "+"
print(cave[0:10, 495:505])
sol = 0

for rain_down in range(100000):
    at_rest = False
    x, y = 500, 0
    while not at_rest and y < 999:
        if cave[y+1, x] == ".":
            y, x = y+1, x
        elif cave[y+1, x-1] == ".":
            y, x = y+1, x-1
        elif cave[y+1, x+1] == ".":
            y, x = y+1, x+1
        else:
            at_rest = True
            cave[y, x] = "o"
            sol += 1
    if y == 999:  # task a
    # if x == 500 and y == 0:   # task b
        break
print(cave[0:10, 495:505])
print(sol)
