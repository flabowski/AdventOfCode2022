with open("./input.txt", 'r') as file:
    rucksacks = file.readlines()
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
score1, score2 = 0, 0
for rucksack in rucksacks:
    n = len(rucksack)//2
    for item in rucksack[:n]:
        if item in rucksack[n:]:
            score1 += letters.find(item)+1
            break

for i in range(1, len(rucksacks), 3):
    for item in rucksacks[i-1]:
        if item in rucksacks[i] and item in rucksacks[i+1]:
            score2 += letters.find(item)+1
            break

print(score1, score2)
