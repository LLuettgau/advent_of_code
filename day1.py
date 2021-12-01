import numpy as np

#part 1
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day1.txt'
data = np.loadtxt(fname)
print(data)

diff_vec = np.diff(data)

sum_diff = np.sum(diff_vec > 0)
print(sum_diff)

#part 2
from numpy.lib.stride_tricks import sliding_window_view

sliding_sum = np.sum(sliding_window_view(data, window_shape = 3), axis = 1)

sliding_sum_diff_vec = np.diff(sliding_sum)
sliding_sum_diff = np.sum(sliding_sum_diff_vec > 0)
print(sliding_sum_diff)