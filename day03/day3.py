def get_gamma_epsilon(lines):
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
            elif line[j] == '0':
                zeros += 1
        if ones > zeros:
            gamma += '1'
            epsilon += '0'
        elif zeros > ones:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '-'
            epsilon += '-'
    return gamma, epsilon


def find_bit_criteria(bit_criteria_oxy, bit_criteria_co2, col, max_col, finished):
    criteria_oxy = []
    criteria_co2 = []
    if len(bit_criteria_oxy) == 1:
        finished[0] = 1
        criteria_oxy = bit_criteria_oxy
    if len(bit_criteria_co2) == 1:
        finished[1] = 1
        criteria_co2 = bit_criteria_co2
    if finished[0] == 1 and finished [1] == 1:
        return bit_criteria_oxy[0], bit_criteria_co2[0]
    if col >= max_col:
        return None, None
    
    if finished[0] == 0:
        gamma, _ = get_gamma_epsilon(bit_criteria_oxy)
        for i in range(len(bit_criteria_oxy)):
            line = bit_criteria_oxy[i]
            if gamma[col] == '-' and line[col] == '1':
                #keep ones if equally common
                criteria_oxy.append(line)
            elif line[col] == gamma[col]:
                criteria_oxy.append(line)

    if finished[1] == 0:
        _, epsilon = get_gamma_epsilon(bit_criteria_co2)
        for i in range(len(bit_criteria_co2)):
            line = bit_criteria_co2[i]
            if epsilon[col] == '-' and line[col] == '0':
                #keep zeros if equally common
                criteria_co2.append(line)
            elif line[col] == epsilon[col]:
                criteria_co2.append(line)

    return find_bit_criteria(criteria_oxy, criteria_co2, col+1, max_col, finished)



with open('test.txt') as file:
    lines = file.read().splitlines()

gamma, epsilon = get_gamma_epsilon(lines)
gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
power_consumption = gamma_dec * epsilon_dec
print("gamma: %d, epsilon: %d -> power consumption: %d" %(gamma_dec, epsilon_dec, power_consumption))

life_support_rating = 0
oxy_gen_rating, co2_scrub_rating = find_bit_criteria(lines, lines, 0, len(lines[0]), [0, 0])
if oxy_gen_rating is not None and co2_scrub_rating is not None:
    life_support_rating = int(oxy_gen_rating, 2) * int(co2_scrub_rating, 2)
    print("life_support_rating: ", life_support_rating)

