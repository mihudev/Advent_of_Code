import timeit
from collections import Counter

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# cards is used to track how many specific cards we have
cards = Counter([x for x in range(0, len(lines))])
total_score = 0
for n, line in enumerate(lines):
    # Extracting numbers and dividing them into winning and held number sets
    line = line.strip().split(':')[1].split('|')
    win = set(int(x) for x in line[0].split())
    num = set(int(x) for x in line[1].split())
    # Using set intersection to generate a winning set and its length
    count = len(win.intersection(num))
    # Updating count for following cards so that update does not go over the data limit
    for next_card in range(min([n+1, len(lines)]), min([n+count+1, len(lines)])):
        cards.update({next_card: cards[n]})

print("Result Part 2:", cards.total())

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")