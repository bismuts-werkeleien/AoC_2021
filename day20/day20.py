import numpy as np
import itertools
from copy import deepcopy

N_ENHANCEMENTS=50
neighbors = [[-1,0,1],[-1,0,1]]


def get_neighbors(x, y, image, border):
    idx = ''
    for i in neighbors[0]:
        for j in neighbors[1]:
            if 0 <= x+j < image.shape[1] and 0 <= y+i < image.shape[0]:
                idx += image[y+i, x+j]
            else:
                idx += border
    return idx



with open('input.txt') as file:
    lines = file.read().splitlines()
algorithm = lines[0]

n_rows = len(lines) - 2
n_cols = len(lines[2])

image = np.full((n_rows, n_cols), dtype=str, fill_value='0')
for i in range(n_rows):
    for j in range(n_cols):
        char = lines[i+2][j]
        if char == '#':
            image[i,j] = '1'

border = '0'
for _ in range(N_ENHANCEMENTS):
    enhanced_image = np.full((image.shape[0]+2, image.shape[1]+2), dtype=str, fill_value=border)
    for y in range(-1, image.shape[0]+1):
        for x in range(-1, image.shape[1]+1):
            #if 1 <= x < image.shape[1]-1 and 1 <= y < image.shape[0]-1:
            #    bin_str = list(itertools.chain(*image[y-1:y+2, x-1:x+2]))
            #    bin_str = ''.join(bin_str)
            #else:
            bin_str = get_neighbors(x,y, image, border)
            index = int(bin_str, 2)
            enhanced_image[y+1,x+1] = '1' if algorithm[index] == '#' else '0'
    image = deepcopy(enhanced_image)
    if algorithm[0] == '#':
        border = '1' if border == '0' else '0'

enhanced_image = enhanced_image.astype(int)
print(np.sum(enhanced_image))