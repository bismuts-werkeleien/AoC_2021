import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

def fold_y(paper, coordinate: int):
    max_iter = max(paper.shape[0] - coordinate, coordinate)
    folded_paper = paper[:coordinate]
    for i in range(1,max_iter):
        folded_paper[coordinate - i] = folded_paper[coordinate - i] | paper[coordinate + i]
    print(folded_paper)
    return folded_paper

def fold_x(paper, coordinate: int):
    print(coordinate, paper.shape[1], paper[:,0])
    max_iter = max(paper.shape[1] - coordinate, coordinate)
    folded_paper = paper[:, :coordinate]
    for i in range(1, max_iter):
        folded_paper[:, coordinate - i] = folded_paper[:, coordinate - i] | paper[:, coordinate + i]
    print(folded_paper)
    return folded_paper

with open('input.txt') as file:
    coordinates = []
    instructions = []
    for line in file:
        line = line.rstrip('\n')
        if len(line) == 0:
            continue
        if not line.startswith('fold'):
            coordinates.append(line.split(','))
        else:
            line = line.lstrip('fold along ')
            instructions.append(line)

coord_arr = np.asarray(coordinates, dtype=int)
x_max = coord_arr[:,0].max()
y_max = coord_arr[:,1].max()

paper = np.zeros((y_max+1,x_max+1), dtype=int)
for x,y in coord_arr:
    paper[y,x] = 1
print(paper)

for i in instructions:
    print(i)
    instruction = i.split('=')
    paper =  fold_y(paper, int(instruction[1])) if instruction[0] == 'y' else fold_x(paper, int(instruction[1]))
    print(paper.sum())
    
