import numpy as np

fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day1.txt'
data = np.loadtxt(fname)
print(data)

diff_vec = np.diff(data)

sum_diff = np.sum(diff_vec > 0)
print(sum_diff)