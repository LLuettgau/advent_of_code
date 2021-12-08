#part 1 - with help from reddit solutions
from statistics import median, mean

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day7.txt'

with open(fname, 'r') as f:
    data = list(map(int, f.readline().strip().split(",")))

median_pos = median(data)
print(int(sum(abs(crab - median_pos) for crab in data)))

#part 2 - again with help from reddit solutions
print(min(sum(abs(crab - pos) * (abs(crab - pos) + 1) / 2 for pos in data) for crab in data)) 
