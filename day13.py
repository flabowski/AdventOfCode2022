with open("./day13/input.txt", 'r') as file:
    data = file.read()


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left > right:
            res = -1  # wrong order
        if left < right:
            res = 1  # right order
        if left == right:
            res = 0  # keep checking
        return res
    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            res = compare(a, b)
            if res:
                return res
        if len(left) > len(right):  # right ran out
            return -1
        if len(left) < len(right):  # left ran out
            return 1
    if isinstance(left, int) and isinstance(right, list):
        res = compare([left], right)
        if res:
            return res
    if isinstance(left, list) and isinstance(right, int):
        res = compare(left, [right])
        if res:
            return res
    else:
        return 0  # contnue


res = 0
list1, list2 = None, None
for k, pairs in enumerate(data.split("\n\n")):
    print("== Pair", k+1, "==")
    pkg1, pkg2 = pairs.split("\n")
    exec("list1 = "+pkg1)
    exec("list2 = "+pkg2)
    right_order = compare(list1, list2) > -1
    if right_order:
        res += k+1
    print(k+1, right_order)
    print()
print(res)


class MyList:
    def __init__(self, the_list):
        self.list = the_list

    def __lt__(self, other):
        return compare(self.list, other.list) > -1


all_lists = [MyList([[2]]), MyList([[6]])]
for k, line in enumerate(data.replace("\n\n", "\n").split("\n")):
    exec("list1 = "+line)
    all_lists.append(MyList(list1))

for i, elem in enumerate(sorted(all_lists)):
    print(elem.l)
    if elem == all_lists[0]:
        a = i+1
    if elem == all_lists[1]:
        b = i+1
print(a, b, a*b)
