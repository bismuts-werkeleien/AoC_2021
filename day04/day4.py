import numpy as np

def apply_call(cur_call: int):
    mask = (bingo_fields == cur_call)
    return mask

def calc_bingos(mask: np.ndarray):
    winner = []
    for i in range(mask.shape[0]):
        col_sums = np.sum(mask[i], axis=0)
        row_sums = np.sum(mask[i], axis=1)
        if 5 in row_sums:
            winner.append(i)
        if 5 in col_sums:
            winner.append(i)
    return list(set(winner))

def calc_score(field: np.ndarray, mask: np.ndarray, winners, cur_call):
    scores = []
    for w in winners:
        unused_values = np.sum(field[w][~mask[w]])
        print(unused_values)
        scores.append(cur_call * unused_values)
    return scores

with open('input.txt') as file:
    lines = file.read().splitlines()

bingo_calls = lines[0].split(',')
bingo_list = []

for i in range(2, len(lines)):
    numbers = lines[i].split()
    if len(numbers) > 0:
        bingo_list.append(numbers)

bingo_fields = np.asarray(bingo_list, dtype=int).reshape((-1, 5, 5))
bingo_masks = np.zeros(bingo_fields.shape, dtype=bool)

bingo_calls = [int(n) for n in bingo_calls]
won_before = False

for c in bingo_calls:
    bingo_masks += apply_call(c)
    winners = calc_bingos(bingo_masks)
    if len(winners) > 0:
        print("winner: ", winners)
        scores = calc_score(bingo_fields, bingo_masks, winners, c)
        if not won_before:
            print("First win: number called ", c, ", score: ", scores)
            won_before = True
        else:
            print("Other win: number_called", c, ", score: ", scores)
        # remove board once it has won
        masks_temp = np.delete(bingo_masks, winners, 0)
        fields_temp = np.delete(bingo_fields, winners, 0)
        bingo_masks = masks_temp
        bingo_fields = fields_temp
        if bingo_masks.shape[0] == 0:
            break