with open("./input.txt", 'r') as file:
    assignments = file.readlines()
answer1, answer2 = 0, 0
for pair in assignments:
    s1, e1, s2, e2 = [int(n) for n in pair.replace("-", ",").split(",")]
    answer1 += (s1-s2) * (e2-e1) >= 0  # both positive or both negative
    answer2 += ((s1 <= s2 <= e1) or (s1 <= e2 <= e1) or (s2 <= s1 <= e2) or (s2 <= e1 <= e2))
print(answer1, answer2)
