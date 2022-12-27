with open("./input.txt", 'r') as file:
    lines = file.readlines()
stacks = [[], [], [], [], [], [], [], [], []]
for line in lines[::-1]:
    if '[' in line:
        for j in range(len(stacks)):
            elem = line[1+j*4]
            if elem != " ":
                stacks[j].append(elem)
for line in lines:
    if line[:4] == 'move':
        for k in range(int(line.split(" ")[1])):
            frm = int(line.split(" ")[3])-1
            to = int(line.split(" ")[5])-1
            stacks[to].append(stacks[frm].pop())
        items = int(line.split(" ")[1])
        frm = int(line.split(" ")[3])-1
        to = int(line.split(" ")[5])-1
        stacks[to] = stacks[to] + stacks[frm][-items:]
        del stacks[frm][-items:]
for stack in stacks:
    print(stack[-1], end="")
