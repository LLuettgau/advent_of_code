#part 1/2 - with help from reddit solutions
import fileinput

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day10.txt'

with open(fname) as f:
    data = f.read().splitlines()

open_char = {'<': '>', '(': ')', '[': ']', '{': '}'}
close_char = {'>': '<', ')': '(', ']': '[', '}': '{'}
scoring1 = {'>': 25137, ')': 3, ']': 57, '}': 1197}
scoring2 = {'>': 4, ')': 1, ']': 2, '}': 3}
result1, result2 = 0, []

for line in data:
    stack = []
    intact_line = True
    for character in line.strip():
        if character in open_char:
            stack.append(character)
        elif character in close_char and stack[-1] == close_char[character]:
            stack.pop()
        else:
            result1 += scoring1[character]
            intact_line = False
            break
    if intact_line:
        total = 0
        while stack:
            x = open_char[stack.pop()]
            total = total * 5 + scoring2[x]
        result2.append(total)
print(result1)
print(sorted(result2)[len(result2)//2])