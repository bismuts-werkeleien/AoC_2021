from collections import Counter

def strlen(n: str):
    return len(n)

def subset(big_set: set, subset: set):
    for i in subset:
        big_set.discard(i)
    return big_set

def build_mapping(candidates_2_3_5: list, candidates_6_9_0: list):
    #  dddd
    # e    a
    # e    a
    #  ffff
    # g    b
    # g    b
    #  cccc

    d = subset(segments_on[7].copy(), segments_on[1])
    gc = subset(subset(segments_on[8].copy(), segments_on[4]), d)
    ef = subset(segments_on[4].copy(), segments_on[1])

    b = set()
    c = set()
    a = set()
    f = set()
    e = set()


    # find segment 6
    for candidate in candidates_6_9_0:
        tmp = set()
        tmp.update(d, gc, ef)
        signal = subset(set(candidate), tmp)
        #print("---")
        #print(tmp,signal, candidate)
        if len(signal) == 1:
            b.update(signal)
            segments_on[6] = tmp.union(b)
    candidates_6_9_0.remove(segments_on[6])
    # find segment 5
    for candidate in candidates_2_3_5:
        tmp = set()
        tmp.update(ef, b, d)
        signal = subset(set(candidate), tmp)
        if len(signal) == 1:
            c.update(signal)
            segments_on[5] = tmp.union(c)
    candidates_2_3_5.remove(segments_on[5])
    # find segment 9
    for candidate in candidates_6_9_0:
        tmp2 = set()
        tmp2.update(d, ef, b, c)
        signal2 = subset(set(candidate), tmp2)
        if len(signal2) == 1:
            a.update(signal2)
            segments_on[9] = tmp2.union(a)
    candidates_6_9_0.remove(segments_on[9])
    # find segment 0
    for candidate in candidates_6_9_0:
        tmp1 = set()
        tmp1.update(d, gc, b, a)
        signal1 = subset(set(candidate), tmp1)
        if len(signal1) == 1:
            e.update(signal1)
            segments_on[0] = tmp1.union(e)
    # find segment 2, 3
    for candidate in candidates_2_3_5:
        tmp1 = set()
        tmp1.update(gc, a, d)
        signal1 = subset(set(candidate), tmp1)
        tmp2 = set()
        tmp2.update(a, b, c, d)
        signal2 = subset(set(candidate), tmp2)
        if len(signal1) == 1:
            f.update(signal1)
            segments_on[2] = tmp1.union(f)
        if len(signal2) == 1:
            f.update(signal2)
            segments_on[3] = tmp2.union(f)
    

def find_first_four(patterns: list):
    strlengths = list(map(strlen, patterns))
    segments_on[1] = patterns[strlengths.index(2)]
    segments_on[4] = patterns[strlengths.index(4)]
    segments_on[7] = patterns[strlengths.index(3)]
    segments_on[8] = patterns[strlengths.index(7)]
    

def find_rest(patterns: list):
    strlengths = list(map(strlen, patterns))
    candidates_6_9_0 = [patterns[index] for index, value in enumerate(strlengths) if value == 6]
    candidates_2_3_5 = [patterns[index] for index, value in enumerate(strlengths) if value == 5]
    build_mapping(candidates_2_3_5, candidates_6_9_0)



with open('input.txt') as file:
    lines = file.read().splitlines()

inputs = [i.split('|') for i in lines]

patterns = []
out_values = []
for i in range(len(inputs)):
    signals = inputs[i][0].split()
    signal_set = [set(j) for j in signals]
    patterns.append(signal_set)
    out_values.append(inputs[i][1].split())

segments_on = {
    0 : [],
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
    8 : [],
    9 : []
}

sum = 0

for i in range(len(out_values)):
    find_first_four(patterns[i])
    find_rest(patterns[i])
    #print(segments_on)

    #strlengths = list(map(strlen, out_values[i]))
    #print(strlengths)
    #counts = Counter(strlengths)

    decoded_output = ''
    for j in out_values[i]:
        for k in range(10):
            if segments_on[k] == set(j):
                decoded_output += str(k)
    print(decoded_output)
    sum += int(decoded_output)

print(sum)