#part 1 - with help from reddit solutions
fname = 'C:\\Users\lenna\Data_Transfer_HHU_Mac\PostDoc\Advent_of_code/Day5.txt'

f = open(fname,"r")    

coordinates = [[coords.strip().split(",") for coords in line.split("->")] for line in f.read().splitlines()]    
coords = {}     
count_diagonals = False  

for coord_idx in coordinates:    
        x_start = int(coord_idx[0][0])
        y_start = int(coord_idx[0][1])
        x_end = int(coord_idx[1][0])
        y_end = int(coord_idx[1][1])

        y_dir = (y_end - y_start) / (abs(y_end - y_start) if abs(y_end - y_start) > 0 else 1)        
        x_dir = (x_end - x_start) / (abs(x_end - x_start) if abs(x_end - x_start) > 0 else 1)     

        if y_end == y_start or x_end == x_start or count_diagonals:                                                   
            end = max(abs(y_end - y_start), abs(x_end - x_start))
            for i in range(end+1):                
                key = (x_start + i * x_dir, y_start + i * y_dir)                                                 
                if key in coords:        
                    coords[key] += 1                
                else:                    
                    coords[key] = 1  

overlap_counter = 0    
for coord_count in coords.values():        
    if coord_count >= 2:            
        overlap_counter += 1    
print(overlap_counter)