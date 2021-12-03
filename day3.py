#part 1
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day3.txt'
with open(fname) as f:
    data = f.read().splitlines()
    
gamma_rate=""
epsilon_rate=""

for row_idx in range(len(data[1])):
		zero_count = 0
		one_count = 0
		for col_idx in range(len(data)):
			if data[col_idx][row_idx] == "0":
				zero_count += 1
			elif data[col_idx][row_idx] == "1":
				one_count += 1
		if one_count > zero_count:
			gamma_rate = gamma_rate + "1"
		elif zero_count > one_count:
			gamma_rate = gamma_rate + "0"

print(int(gamma_rate))
print(int(gamma_rate,2)) #convert to decimal 

for num in gamma_rate:
		if num == "0":
			epsilon_rate = epsilon_rate + "1"
		elif num == "1":
			epsilon_rate = epsilon_rate + "0"

print(int(epsilon_rate))
print(int(epsilon_rate,2)) #convert to decimal 

print(int(epsilon_rate, 2) * int(gamma_rate, 2))
