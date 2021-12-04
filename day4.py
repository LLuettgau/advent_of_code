fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day4.txt'

with open(fname) as f:
    data = f.read()

numbers, *boards = data.split('\n\n')

numbers = [int(x) for x in numbers.split(',')]
boards = [[[int(n) for n in row.split()] for row in board.splitlines()] for board in boards]

used_numbers, winning_boards = set(numbers[:1]), set()

for i in numbers:
	used_numbers.add(i)
	for (k, step) in enumerate(boards):
		if k in winning_boards: 
			continue
		if any(all(n in used_numbers for n in row) for row in step) or any(all(n in used_numbers for n in col) for col in zip(*step)):
			winning_boards.add(k)
			if len(winning_boards) == 1 or len(winning_boards) == len(boards): 
			    print(sum(sum(n for n in line if n not in used_numbers) for line in step) * i)
