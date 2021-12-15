import numpy as np

def explore_basin(i, j, visited, basin_size):
    if visited[i,j]:
        return basin_size
    visited[i][j] = 1
    basin_size += 1
    basin_size = explore_basin(i, j-1, visited, basin_size)
    basin_size = explore_basin(i, j+1, visited, basin_size)
    basin_size = explore_basin(i+1, j, visited, basin_size)
    basin_size = explore_basin(i-1, j, visited, basin_size)
    return(basin_size)

with open('input.txt') as file:
    lines = file.read().splitlines()

# pad the topography matrix with the maximum value (9)
topography = np.full((len(lines)+2,len(lines[0])+2), fill_value=9, dtype=int)

for i in range(len(lines)):
    numbers = lines[i]
    for j in range(len(numbers)):
        topography[i+1][j+1] = int(numbers[j])
    
low_points = []
basin_sizes = []
borders = np.zeros(topography.shape, dtype=int)
borders[topography==9] = 1

for i in range(1, topography.shape[0]-1):
    for j in range(1, topography.shape[1]-1):
        point = topography[i][j]
        up = topography[i-1][j]
        down = topography[i+1][j]
        left = topography[i][j-1]
        right = topography[i][j+1]

        if point < up and point < down and point < left and point < right:
            basin_size = 0
            low_points.append(point)
            basin_size = explore_basin(i, j, borders, basin_size)
            basin_sizes.append(basin_size)

print(low_points)
risk_level = [i+1 for i in low_points]
risk_sum = sum(risk_level)
print(risk_sum)
print(basin_sizes)
basin_sizes.sort()
largest = basin_sizes[-3] * basin_sizes[-2] * basin_sizes[-1]
print(largest)