#part 1 - with help from reddit solutions
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day8.txt'

counter = 0
with open(fname, "r") as f:
    for line in f:
        segments, digits = line.strip().split("|")
        digits = digits.strip().split(" ")
        for d in digits:
            if len(d) in (2, 4, 3, 7):
                counter += 1

print(counter)
