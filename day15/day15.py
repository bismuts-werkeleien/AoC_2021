from copy import deepcopy
import sys

# part 1 or 2
PART = 2

def traverse_neighbors(i: int, j: int, parent_cost: int):
    cur_val = risk_level[i][j]
    #print(cur_val, parent_cost, cave[i,j], i, j)
    edge_val = parent_cost + cave[i][j]
    #print(cur_val, edge_val)
    changed = False
    if edge_val < cur_val:
        risk_level[i][j] = edge_val
        changed = True
    return changed


with open('input.txt') as file:
    lines = file.read().splitlines()

n_rows = len(lines)
n_cols = len(lines[0])
cave = [[0]*n_cols for _ in range(n_rows)]

if PART == 1:
    for i in range(n_rows):
        for j in range(n_cols):
            cave[i][j] = int(lines[i][j])

if PART == 2:
    #input is 5 times larger:
    rows = []
    for r in range(len(lines)):
        row = [int(x) for x in lines[r]]
        new_row = deepcopy(row)
        for i in range(4):
            new_row = [1 if x == 9 else x + 1 for x in new_row]
            row += new_row
        rows.append(row)
    real_cave = deepcopy(rows)
    for i in range(1,5):
        for row in rows:
            real_cave.append([x+i if x+i < 10 else x + i - 9 for x in row])
    n_cols *= 5
    n_rows *= 5
    cave = deepcopy(real_cave)

#pad risk level at upper and left border for later comparisons
risk_level = [[sys.maxsize]*n_cols for _ in range(n_rows)]

visited = [[0]*n_cols for _ in range(n_rows)]
queue = []

# start field is not entered (no costs apply):
risk_level[0][0] = 0
curr_node = (0,0)
queue.append((0,0,0))
visited[0][0] = 1

#while(len(queue)>0):
while(any(0 in vs for vs in visited)):
    curr_node = queue.pop()
    i = curr_node[0]
    j = curr_node[1]
    if i == n_rows-1 and j == n_cols-1:
        continue
    neighbors = []
    if i < n_rows-1:
        neighbors.append((i+1,j))
    if j < n_cols-1:
        neighbors.append((i,j+1))
    if i > 0:
        neighbors.append((i-1,j))
    if j > 0:
        neighbors.append((i,j-1))

    for n,m in neighbors:
        traverse_neighbors(n, m, risk_level[i][j])
        if not visited[n][m]:
            visited[n][m] = 1
            queue.append((n,m,risk_level[n][m]))
    queue.sort(key=lambda x: x[2], reverse=True)
    
print(risk_level[-1][-1])
