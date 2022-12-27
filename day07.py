with open("./input.txt", 'r') as file:
    data = file.readlines()

sizes = {}
folders = {}
path = "root"
for line in data:
    if line.startswith("$ cd .."):
        path = "/".join(path.split("/")[:-1])
    elif line.startswith("$ cd "):
        path += "/"+line.split()[2]
        sizes[path] = 0
        folders[path] = []
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("dir"):
        folders[path].append(line.split()[1])
    else:
        sizes[path] += int(line.split()[0])


def get_size(pth):
    res = sizes[pth]
    for subf in folders[pth]:
        res += get_size(pth+"/"+subf)
    return res


print(sum(i for i in map(get_size, sizes.keys()) if i <= 100000))

used = get_size('root//')
free = 70000000-used
need = 30000000-free
smallest = get_size('root//')
for s in map(get_size, sizes.keys()):
    smallest = s if s > need and s < smallest else smallest
print(smallest)
