#part 1/2 - with help from reddit solutions
from collections import Counter

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day14.txt'
from collections import Counter

with open(fname) as f:
    data = [line.strip() for line in f.readlines()]

template = data[0]
letters = Counter(template)
pairs = Counter([a+b for a,b in zip(template,template[1:])])

rules = dict()
for line in data[2:]:
    a,b,c = line[0],line[1],line[-1]
    rules[a+b] = c

for _ in range(40): #needs to be set to 10 if part 1
    oldpairs = pairs.copy()
    for (a,b),c in rules.items():
        count = oldpairs[a+b]
        pairs[a+b] -= count
        pairs[a+c] += count
        pairs[c+b] += count
        letters[c] += count

print(letters.most_common())
print(letters.most_common()[0][1]-letters.most_common()[-1][1])