from math import floor

with open("./input.txt", 'r') as file:
    data = file.read()


class Monkey():
    inspections = 0

    def __init__(self, name, items, operation, test, if_true, if_false):
        self.name = name
        self.items = items
        _, _, a, operator, b = operation.split()
        if operator == "+":
            self.operation = lambda x: x+int(b)
        elif operator == "*" and b == "old":
            self.operation = lambda x: x*x
        elif operator == "*":
            self.operation = lambda x: x*int(b)
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

    def inspect(self):
        self.inspections += 1


monkeys = []
for m in data.split("\n\n"):
    lines = m.split("\n")
    name = int(lines[0].split()[-1][:-1])
    items = [int(a) for a in lines[1].replace("  Starting items: ", "").split(", ")]
    operation = lines[2].replace("  Operation: ", "")
    test = int(lines[3].replace("  Test: divisible by ", ""))
    thow_if_true = int(lines[4].replace("    If true: throw to monkey ", ""))
    thow_if_false = int(lines[5].replace("    If false: throw to monkey ", ""))
    monkeys.append(Monkey(name, items, operation, test, thow_if_true, thow_if_false))

# task b
kgv = 1
for monkey in monkeys:
    kgv *= monkey.test

# for round in range(20):  # 20 task a
for round in range(10000):  # 10000 task b
    for monkey in monkeys:
        # print("Monkey", monkey.name, ":")
        for i in range(len(monkey.items)):
            monkey.inspect()
            item = monkey.items.pop(0)
            worry_level = monkey.operation(item)
            worry_level = worry_level % kgv  # task b
            # worry_level = floor(worry_level/3)  # task a
            condition = worry_level % monkey.test == 0
            if condition:
                send_to = monkey.if_true
            else:
                send_to = monkey.if_false
            # print("    Item with worry level", worry_level, "is thrown to monkey", send_to)
            monkeys[send_to].items.append(worry_level)
print(monkeys[0].items)
print(monkeys[1].items)
print(monkeys[2].items)
print(monkeys[3].items)
inspections = [monkey.inspections for monkey in monkeys]
inspections.sort()
print(inspections[-1]*inspections[-2])
