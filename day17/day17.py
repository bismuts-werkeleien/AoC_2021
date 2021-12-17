
def in_target(x,y):
    if target[0] <= x and x <= target[1] and target[3]>= y and y >= target[2]:
        #print(x,y)
        return True
    return False

def step(position: tuple, parameters: tuple):
    x = position[0] + parameters[0]
    y = position[1] + parameters[1]
    x_vel = 0
    y_vel = 0
    if parameters[0] > 0:
        x_vel = parameters[0] - 1
    elif parameters[0] < 0:
        x_vel = parameters[0] + 1
    y_vel = parameters[1] - 1
    #print(x,y, position,(x_vel,y_vel))
    return (x,y), (x_vel, y_vel)

def throw(position, parameters, target_velocity, target_altitude, hits):
    max_altitude = target_altitude[0] - 100
    while(True):
        position, parameters = step(position, parameters)
        max_altitude = max(max_altitude, position[1])
        #print('>', max_altitude, position, parameters)
        if in_target(position[0], position[1]):
            hits += 1
            return max_altitude, hits
        # end this if we over/undershoot target
        if position[1] < target_altitude[0] or position[0] > target_velocity[1]:
            return target_altitude[0] - 100, hits

with open('input.txt') as file:
    line = file.read().splitlines()
line = line[0].split()
target_x = line[2].split('..')
target_x[0] = target_x[0].lstrip('x=')
target_x[1] = target_x[1].rstrip(',')
target_y = line[3]. split('..')
target_y[0] = target_y[0].lstrip('y=')

target = [int(x) for x in target_x + target_y]
print(target)

start = (0,0)
max_altitude = target[2] - 100
hits = 0
for x in range(0, target[1]+1):
    for y in range(target[2]*2, target[2]*(-2)):
        curr_altitude, hits = throw(start, (x,y), (target[0], target[1]), (target[2], target[3]), hits)
        max_altitude = max(curr_altitude, max_altitude)
print("Max altitude: ", max_altitude, "- Overall target hits: ", hits)