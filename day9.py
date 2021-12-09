#part 1 - with help from reddit solutions
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day9.txt'

with open(fname) as f:
    height_map = []
    for line in f.read().splitlines():
        height_map.append([int(i) for i in line])

h = len(height_map)
w = len(height_map[0])

def adjacent(j, i):
    return set([(abs(j-1), i), (j, abs(i-1)), (j+1 - 2*(j==(h-1)), i), (j, i+1 - 2*(i==(w-1)))])

risk_sum = 0
low_points = []
for j in range(h):
    for i in range(w):
        if all([height_map[j][i] < height_map[y][x] for y, x in adjacent(j, i)]):
            risk_sum += 1 + height_map[j][i]
            low_points.append((j, i))

print(risk_sum)