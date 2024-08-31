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

# Loop iterates over all seeds, blocks and substitutions in blocks.
# If seed matches substitution, it is replaced with a new one,
# otherwise it remains the same for checks in next block
results = []
for seed in map(int, blocks[0][0].split(':')[1].strip().split(' ')):
    for b_num in range(1, len(blocks)):
        for substitution in blocks[b_num][1:]:
            new_val, start, span = map(int, substitution.split(' '))
            if seed in range(start, start + span):
                seed += new_val - start
                break
    results.append(seed)

# Lowest value is the final result
print("Result Part 1:", sorted(results)[0])

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")