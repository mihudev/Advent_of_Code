import timeit

start_t = timeit.default_timer()

# Input has 2 additional \n at the end to fit reading blocks
with open('input.txt','r') as f:
    lines = f.readlines()

# Each part of input is held in seprate block / part of blocks[] with seeds in blocks[0]
blocks = []
block = []
for line in lines:
    if line == '\n':
        blocks.append(block)
        block = []
        continue
    block.append(line.strip())

# Extracting seeds from data
seeds = [int(x) for x in blocks[0][0].split(' ')[1:]]

# Constructing seed ranges from seeds
ranges = []
for n in range(0, len(seeds), 2):
    ranges.append((seeds[n], seeds[n] + seeds[n+1]))

# Loop iterates over all blocks, ranges and substitutions in blocks
for block in blocks[1:]:
    new_seeds = []
    for range in ranges:
        for substitution in block[1:]:
            x1, x2 = range
            # Substitution example:
            # 3600371492 4267529956 27437340
            # start of new value range, start of old value range, length of range
            new, y1, d = map(int, substitution.split(" "))
            y2 = y1 + d
            # No overlap, no action
            if x1 >= y2 or x2 <= y1:
                continue
            # Full overlap, only new seed is created
            if x1 >= y1 and x2 <= y2:
                new_seeds.append((x1 + new - y1, x2 + new - y1))
                break
            # Partial overlap, new seed is created and a remaining seed range appended to current ranges
            if x1 >= y1 and x2 > y2:
                new_seeds.append((x1 + new - y1, new + d))
                ranges.append((y2, x2))
                break
        else:
            # Range did not match any substitution, added to new seeds and remains the same for the next block
            new_seeds.append((x1, x2))
    # Set new ranges for the next block
    ranges = new_seeds

# Sorting final ranges by first value, the lowest one is the result
print("Result Part 2:", sorted(ranges, key = lambda range: range[0])[0][0])

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")