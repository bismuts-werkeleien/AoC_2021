from collections import Counter
import itertools as it
from copy import deepcopy

def insert_polymer(slice: tuple, quantity: int):
    insertion = rules[''.join(slice)]
    polymer1 = (slice[0], insertion)
    polymer2 = (insertion, slice[1])
    counts[insertion] += quantity
    return [polymer1, polymer2]


with open('input.txt') as file:
    lines = file.read().splitlines()

template = [i for i in lines[0]]
rules_list = [lines[i].split(' -> ') for i in range(2, len(lines))]
rules = {rules_list[i][0] : rules_list[i][1] for i in range(len(rules_list))}
print(rules)

counts = Counter(template)
pairs = list(zip(template, template[1::]))
pair_count = Counter(pairs)

for _ in range(40):
    new_pair_count = Counter()
    for p in pair_count:
        inserted_polymers = insert_polymer(p, pair_count[p])
        for polymer in inserted_polymers:
            new_pair_count[polymer] += pair_count[p]

    pair_count = deepcopy(new_pair_count)


print(counts)
most_c = counts.most_common()[0]
print(most_c)
least_c = counts.most_common()[-1]
print(least_c)
quantity = most_c[1]-least_c[1]
print(quantity)
