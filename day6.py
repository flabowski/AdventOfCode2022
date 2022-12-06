with open("./input.txt", 'r') as file:
    datastream = file.readlines()[0]
n = 14
for i in range(len(datastream)-n+1):
    char_set = {*datastream[i:(i+n)]}
    if len(char_set) == n:
        print(i+n, datastream[i:(i+n)])
        break
