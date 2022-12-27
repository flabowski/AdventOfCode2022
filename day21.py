with open("./input.txt", 'r') as file:
    lines = file.readlines()
monkeys = {}
stack = []
for line in lines:
    m, o = line.split(": ")
    if len(o) > 5:
        m1, op, m2 = o.split()
        stack.append((m, m1, op, m2))
    else:
        monkeys[m] = int(o)
    print(line)

found_root = False
while not found_root:
    for i, elem in enumerate(stack):
        if elem:
            m, m1, op, m2 = elem
            if m1 in monkeys.keys():
                if m2 in monkeys.keys():
                    if op == "+":
                        monkeys[m] = monkeys[m1]+monkeys[m2]
                    if op == "-":
                        monkeys[m] = monkeys[m1]-monkeys[m2]
                    if op == "*":
                        monkeys[m] = monkeys[m1]*monkeys[m2]
                    if op == "/":
                        monkeys[m] = monkeys[m1]/monkeys[m2]
                    print(m, monkeys[m])
                    stack[i] = False
                    if m == "root":
                        found_root = True
monkeys[m] = monkeys[m1] == monkeys[m2]

monkeys = []
for line in lines:
    m, o = line.split(": ")
    if m != "humn":
        monkeys.append((m, o))
    if m == "root":
        equation = o[:4] + "==" + o[-5:]

for i in range(200):
    for m, o in monkeys:
        c = m in equation
        equation = equation.replace(m, "("+o.strip()+")")
        if c:
            print(m, o.strip())
            print(equation)
            print()


# for humn in range(1000000000):
#     cond = eval(equation)
#     # print(humn, cond)
#     if cond:
#         print("humn = ", humn)
#         break

equation = equation.replace("==", "-")
humn = x_1 = 1
y_1 = eval(equation)
humn = x_2 = 100
y_2 = eval(equation)
for i in range(10):
    humn = x_3 = (0 - y_1)/(y_2 - y_1)*(x_2 - x_1)+x_1
    y_3 = eval(equation)
    print(x_3, y_3)
    x_1, y_1 = x_2, y_2
    x_2, y_2 = x_3, y_3
