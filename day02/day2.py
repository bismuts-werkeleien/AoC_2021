with open('input.txt') as file:
    commands = [i.split(' ') for i in file.read().splitlines()]

horizontal = 0
depth = 0
aim = 0

for i in range(len(commands)):
    command = commands[i]
    if command[0] == 'forward':
        x = int(command[1])
        horizontal += x
        depth += (aim * x)
    if command[0] == 'up':
        aim -= int(command[1])
    if command[0] == 'down':
        aim += int(command[1])

print(depth, horizontal, depth*horizontal)
