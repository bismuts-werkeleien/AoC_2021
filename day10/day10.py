with open('input.txt') as file:
    lines = file.read().splitlines()

illegal_characters_found = []
missing_characters_added = []
missing_characters_list = []

brackets_mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

for i in lines:
    stack = []
    line = i
    missing_characters_added = []
    discard_line = False
    for j in range(len(line)):
        char = line[j]
        #print(stack)
        if char == '(' or char == '[' or char == '<' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '>' or char == '}' :
            char_expected = brackets_mapping[stack[-1]]
            if char_expected != char:
                print("Expected ", char_expected, ", but found ", char, " instead.")
                illegal_characters_found.append(char)
                discard_line = True
                break
            else:
                stack.pop()
    if not discard_line and len(stack) > 0:
        # line is missing characters
        for j in range(len(stack)):
            char_open = stack.pop()
            missing_characters_added.append(brackets_mapping[char_open])
        missing_characters_list.append(missing_characters_added)
        print("Complete by adding ", missing_characters_added)

points_illegal = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
points_incomplete = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

awarded_illegal = 0
for i in illegal_characters_found:
    awarded_illegal += points_illegal[i]
print("From missing closing brackets: ", awarded_illegal)

awarded_incomplete = [0 for i in range(len(missing_characters_list))]
for i in range(len(missing_characters_list)):
    for j in missing_characters_list[i]:
        awarded_incomplete[i] *= 5
        awarded_incomplete[i] += points_incomplete[j]
print("From autocompletion: ", awarded_incomplete)
awarded_incomplete.sort()
middle_score = awarded_incomplete[len(awarded_incomplete)//2]
print("Resulting middle score: ", middle_score)