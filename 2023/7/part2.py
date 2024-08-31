from collections import Counter
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.read()

# Tuples for card replacement needed for proper sorting
values = [('A', 'e'), ('K', 'd'), ('Q', 'c'), ('J', '0'), ('T', 'a')]
# Replacing cards with their values
for x in values:
        lines = lines.replace(x[0], x[1])
lines = lines.split('\n')

hands = []
for line in lines:
    hand, val = line.split(' ')
    count = Counter(hand)                                   # Counting cards
    jokers = count['0'] if count.get('0') != None else 0    # Find and assign jokers number
    if jokers in range(1, 5):                               # If there are 1-4 jokers, remove jokers from counter and add them to the most common card
        del count['0']
        count = sorted(count.values(), reverse=True)
        count[0] += jokers
    else:                                                   # If there are 0 or 5 jokers do not remove jokers from counter
        count = sorted(count.values(), reverse=True)

    match count:
        case 5,:                # Five of a kind
            card_type = '7'
        case 4, 1:              # Four of a kind
            card_type = '6'
        case 3, 2:              # Full house
            card_type = '5'
        case 3, *_:             # Three of a kind
            card_type = '4'
        case 2, 2, 1:           # Two pairs
            card_type = '3'
        case 2, *_:             # One pair
            card_type = '2'
        case 1, *_:             # None
            card_type = '1'
    hands.append((card_type + hand, int(val)))              # Adding card_type in front of card values for sorting

result = 0
for n, hand in enumerate(sorted(hands), 1):
    result += n * hand[1]

print("Result Part 2:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")