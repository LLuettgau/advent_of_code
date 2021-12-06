#part 1/2 - again with help from reddit solutions
import numpy as np

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day6.txt'

data, day_count = open(fname).read(), 256 #need to change to 80 if part 1

fishes = [data.count(str(i)) for i in range(0,9)]

for i in range(day_count):
    fishes = fishes[1:] + fishes[:1]
    fishes[6] += fishes[8]
print(sum(fishes))
