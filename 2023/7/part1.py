from collections import Counter
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# Tuples for card replacement needed for proper sorting
values = [('A', 'e'), ('K', 'd'), ('Q', 'c'), ('J', 'b'), ('T', 'a')]
hands = []
for line in lines:
    hand, val = line.strip().split(' ')
    for x in values:                                        # Replacing cards with their values
        hand = hand.replace(x[0], x[1])
    count = sorted(Counter(hand).values(), reverse=True)    # Counting and sorting from most to least common card
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
        case 2, 1, *_:          # One pair
            card_type = '2'
        case 1, *_:             # None
            card_type = '1'
    hands.append((card_type + hand, int(val)))              # Adding card_type in front of card values for sorting

result = 0
for n, hand in enumerate(sorted(hands), 1):
    result += n * hand[1]

print("Result Part 1:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")