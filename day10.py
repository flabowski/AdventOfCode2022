with open("./input.txt", 'r') as file:
    program = file.readlines()


def tick(cycle, x, solution):
    cycle += 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        solution += x*cycle
    return cycle, solution


def draw(cycle, x):
    sprite = [x-1, x, x+1]
    if cycle % 40 == 0:
        print()
    if cycle % 40 in sprite:
        print("#", end="")
    else:
        print(" ", end="")


cycle = 0
solution = 0
x = 1
for line in program:
    if line.strip() == "noop":
        draw(cycle, x)
        cycle, solution = tick(cycle, x, solution)
    else:
        operation, value = line.strip().split()
        for j in range(2):
            draw(cycle, x)
            cycle, solution = tick(cycle, x, solution)
        x += int(value)
print(solution)
