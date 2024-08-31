import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# Maximum values for each color
colors = {
    'r': 12,
    'g': 13,
    'b': 14
}

total = 0
for game, line in enumerate(lines, 1):
    for val, color in re.findall('(\d+) (\w)', line):   # Extract (value, color) pairs
        if int(val) > colors[color]:                    # Break loop if value does not meet condition
            break
    else:
        total += game                                   # Add game number otherwise
print("Result Part 1:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")
