#part 1 - with help from reddit solutions
import networkx as nx

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day15.txt'

with open(fname) as f:
     data = [list(map(int, line.strip())) for line in f.readlines()]

idx = len(data) - 1

G = nx.DiGraph()
for y in range(len(data)):
    for x in range(len(data)):
        G.add_node((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x_, y_ = x + dx, y + dy
            if 0 <= x_ < len(data) and 0 <= y_ < len(data):
                G.add_edge((x, y), (x_, y_), weight=data[y_][x_])

path = nx.shortest_path(G, source=(0, 0), target=(idx, idx), weight='weight')
sum_risk = sum(data[y][x] for x, y in path[1:])
print(sum_risk)