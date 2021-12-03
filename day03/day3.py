with open('input.txt') as file:
    lines = file.read().splitlines()

strlen = len(lines[0])
gamma = ''
epsilon = ''

for j in range(strlen):
    ones = 0
    zeros = 0
    for i in range(len(lines)):
        line = lines[i]
        # print(line, j, line[j] == '1')
        if line[j] == '1':
            ones += 1
        else:
            zeros += 1
    if ones > zeros:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

print(gamma, epsilon)
gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
power_consumption = gamma_dec * epsilon_dec
print(gamma_dec, epsilon_dec, power_consumption)
