#part 1 - with help from reddit solutions
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day12.txt'

G = dict()
with open(fname) as f:
    for line in f.readlines():
        starting_state,terminal_state = line.strip().split('-')
        if starting_state not in G:
            G[starting_state] = []
        if terminal_state not in G:
            G[terminal_state] = []
        G[starting_state] += [terminal_state]
        G[terminal_state] += [starting_state]

paths = [['start']]
completepaths = []

while paths:
    path = paths.pop()
    final_cave = path[-1]
    neighbors = G[final_cave]
    for cave in neighbors:
        if cave == 'end':
            completepaths.append(path+[cave])
        elif (cave.isupper()) or (cave not in path):
            paths.append(path+[cave])

print(len(completepaths))

#part 2
paths = [(['start'],True)]
completepaths_2 = []

while paths:
    path,flag = paths.pop()
    final_cave = path[-1]
    neighbors = G[final_cave]
    for cave in neighbors:
        if cave == 'end':
            completepaths_2.append((path+[cave],flag))
        elif cave == 'start':
            continue
        elif (cave.isupper()) or (cave not in path):
            paths.append((path+[cave],flag))
        elif flag:
            paths.append((path+[cave],False))

print(len(completepaths_2))