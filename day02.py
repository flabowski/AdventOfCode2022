with open("./input.txt", 'r') as file:
    strategy_guide = file.readlines()

value = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}  # 1, 2, 3 = R, P, S
result = {-2: 6, -1: 0, 0: 3, 1: 6, 2: 0}  # 6, 0, 3 = W, L, D

score1, score2 = 0, 0
for game in strategy_guide:
    elve = value[game[0]]
    me1 = value[game[2]]
    if game[2] == "X":
        me2 = 3 if game[0] == "A" else elve-1
    elif game[2] == "Z":
        me2 = 1 if game[0] == "C" else elve+1
    else:
        me2 = elve
    score1 += result[me1-elve] + me1
    score2 += result[me2-elve] + me2
print(score1, score2)
