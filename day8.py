import numpy as np
trees = np.genfromtxt("./input.txt", delimiter=1)


def check(row, tree):
    view_blocked = np.where(row >= tree)[0]
    return view_blocked[0]+1 if len(view_blocked) > 0 else len(row)


is_visible = trees < 0
score = np.ones_like(trees)
for i, row in enumerate(trees):
    for j, tree in enumerate(row):
        is_visible[i, j] = (np.all(trees[:i, j] < tree) or
                            np.all(trees[i, :j] < tree) or
                            np.all(trees[(i+1):, j] < tree) or
                            np.all(trees[i, (j+1):] < tree))
        score[i, j] *= check(trees[:i, j][::-1], tree)
        score[i, j] *= check(trees[i, :j][::-1], tree)
        score[i, j] *= check(trees[(i+1):, j], tree)
        score[i, j] *= check(trees[i, (j+1):], tree)

print(is_visible.sum())
print(score.max())
