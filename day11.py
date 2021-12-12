#part 1/2 - with help from reddit solutions
from scipy import signal
import numpy as np

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day11.txt'

num_steps = 1000 #100 for part 1
flashes = 0

data = open(fname,'r').read().replace('\n','')
arr = np.array([int(n) for n in data]).reshape(10,10)

for step in range(num_steps):
    arr += np.ones(arr.shape, dtype=int)
    dx = signal.convolve2d(np.array(arr > 9, dtype=int), np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1))), mode='same')
    while dx.sum() > 0:
        flashed = arr > 9
        flashes += flashed.sum()
        arr[flashed] = -1000
        arr += dx
        dx = signal.convolve2d(np.array(arr > 9, dtype=int), np.array(((1, 1, 1), (1, 0, 1), (1, 1, 1))), mode='same')
    flashed = arr < 0
    arr[flashed] = 0

    if flashed.sum() == arr.size:
        print(step+1)
        break

print(flashes)