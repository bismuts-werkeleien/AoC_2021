import numpy as np
from math import ceil, floor

with open('test.txt') as file:
    line = file.read().splitlines()

lines = line[0].split(',')
positions = [int(i) for i in lines]
positions.sort()
median = positions[len(positions)//2]
print("Best position for part 1: ", median)
pos_arr = np.asarray(positions, dtype=int)
# for test input, best postition is ceil(pos_arr.mean())
mean = floor(pos_arr.mean())
print("Best position for part 2: ", mean)
dists1 = abs(pos_arr - median)
dists2 = abs(pos_arr - mean)
max_dist = dists2[-1]
max_dist1 = dists1[-1]

fuel = [i for i in range(1,max_dist+1)]
fuel = np.asarray(fuel, dtype=int)

fuel1 = [i for i in range(1,max_dist1+1)]
fuel1 = np.asarray(fuel1, dtype=int)
fuel_spent1 = dists1.sum()
fuel_spent2 = [fuel[0:dists2[x]] for x in range(len(dists2))]
fuel_old = [fuel1[0:dists1[x]] for x in range(len(dists1))]
fuel_spent2 = np.concatenate(fuel_spent2, axis=None)
fuel_old = np.concatenate(fuel_old, axis=None)
fuel_spent2 = fuel_spent2.sum()
fuel_old = fuel_old.sum()
print("Fuel spent for part 1: ", fuel_spent1)
print("Fuel spent with old distance: ", fuel_old)
print("Fuel spent for part 2: ", fuel_spent2)