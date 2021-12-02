import numpy as np
import pandas as pd

#part 1
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day2.txt'

df = pd.read_csv(fname, sep=" ", header=None, names=['direction', 'mag'])

print(df)

HPos=0
VPos=0

for index, row in df.iterrows():
    if row['direction'] == "forward":
        HPos = HPos + row['mag']
    if row['direction'] == "down":
        VPos = VPos + row['mag']
    if row['direction'] == "up":
        VPos = VPos - row['mag']

print("Horizontal: " + str(HPos))
print("Vertical: " + str(VPos))
print("Position: " + str(HPos * VPos))

#part 2
aim=0
depth=0
HPos=0

for index, row in df.iterrows():
    if row['direction'] == "forward":
        HPos = HPos + row['mag']
        depth = depth + aim * row['mag']
    if row['direction'] == "down":
        aim = aim + row['mag']
    if row['direction'] == "up":
        aim = aim - row['mag']

print("Horizontal: " + str(HPos))
print("depth: " + str(depth))
print("result: " + str(HPos * depth))

