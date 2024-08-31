import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

total = 0
for game, line in enumerate(lines):
    colors = {'r': 0, 'g': 0, 'b': 0}                   # Initial vlues for each color
    for val, color in re.findall('(\d+) (\w)', line):   # Extract (value, color) pairs
        if int(val) > colors[color]:
            colors.update({color: int(val)})            # Update max value for a given color
    total += colors['r'] * colors['g'] * colors['b']    # Add product of max vlues to the total
print("Result Part 2:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")
