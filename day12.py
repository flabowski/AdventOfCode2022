import numpy as np
grid = np.genfromtxt("./day12/input.txt", delimiter=1, dtype=str)
rs, cs = np.where(grid == "S")
rs, cs = rs[0], cs[0]
letters = "SabcdefghijklmnopqrstuvwxyzE"
visited = np.zeros(grid.shape, dtype=bool)


def check(r, c, h):
    inside_grid = (0 <= r < grid.shape[0]) and (0 <= c < grid.shape[1])
    if inside_grid:
        dh = letters.find(grid[r, c])-letters.find(h)
        if dh <= 1 and not visited[r, c]:
            visited[r, c] = True
            return True
    return False


def explore(path, queue):
    r, c = rs, cs
    for a, b in path:
        r, c = r+a, c+b
    altitude = grid[r, c]
    for a, b in zip([1, -1, 0, 0], [0, 0, 1, -1]):  # ["^", "v", "<", ">"]
        if check(r+a, c+b, altitude):
            queue.append(path + [(a, b)])
    return altitude


shortest_path = 99999
for rs in range(grid.shape[0]):
    for cs in range(grid.shape[1]):
        if grid[rs, cs] == "a":
            visited[:] = 0
            print(rs, cs)
            n_explored = 0
            queue = [[]]
            h = "S"
            while h != "E" and len(queue) > 0:
                path = queue.pop(0)
                h = explore(path, queue)
                n_explored += 1
            print(len(path), n_explored, h)
            if h == "E" and len(path) < shortest_path:
                shortest_path = len(path)
print(shortest_path)
