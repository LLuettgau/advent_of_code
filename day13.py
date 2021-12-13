#part 1/2 - with help from reddit solutions
import numpy as np
from parse import findall

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day13.txt'

data = open(fname).read()
points = np.zeros((9999,9999), bool)

for x,y in findall('{:d},{:d}', data):
    points[y,x] = True

for axis, a in findall('{:l}={:d}', data):
    if axis == 'x': points = points[:,:a] | points[:,2*a:a:-1]
    if axis == 'y': points = points[:a,:] | points[2*a:a:-1,:]
    print(points.sum())

print(np.array2string(points, separator='',
    formatter = {'bool':{0:' ',1:'█'}.get}))