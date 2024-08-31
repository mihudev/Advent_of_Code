import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    codes = f.readline().split(',')

boxes = [[] for _ in range(256)]

def calculate_HASH(label):
    value = 0
    for symbol in label:
        value = ((value + ord(symbol)) * 17) % 256
    return value

def remove_lens(box, lens):
    check_box = []
    check_box.extend([tup for tup in boxes[box] if tup[0] == lens[0]])
    if check_box != []:
        boxes[box].remove(check_box[0])

def add_lens(box, lens):
    check_box = []
    check_box.extend([tup for tup in boxes[box] if tup[0] == lens[0]])
    if check_box != []:
        removed = boxes[box].index(check_box[0])
        boxes[box].remove(check_box[0])
        boxes[box].insert(removed, tuple((lens[0], lens[1])))
    else:
        boxes[box].append(lens)

for code in codes:
    lens = tuple(re.split('-|=', code))
    box = calculate_HASH(lens[0])
    if '=' in code:
        add_lens(box, lens)
    else:
        remove_lens(box, lens)

result_part_2 = 0
for n, box in enumerate(boxes):
    for m, lens in enumerate(box):
        result_part_2 += (n+1) * (m+1) * int(lens[1])

print("Result Part 2: ", result_part_2)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")