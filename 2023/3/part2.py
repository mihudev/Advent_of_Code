import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# stars stores stars' position in dict: line number and index in that line (both indx 0)
stars = {}

for n, line in enumerate(lines):
    for star in re.finditer('\*', line):
        stars[(n, star.start())] = []

for n, line in enumerate(lines):
    for number in re.finditer('\d+', line):                                 # Iterating over all numbers in line
        start, end, value = number.start(), number.end(), number.group()    # Coords for current number
        for row in range(-1, 2):                                            # Finding * in lines relative to current number: above, current and below
            for star in re.finditer('\*', lines[n+row][start-1 : end+1]):   # Finding * within 1 position from number
                stars[(n+row, star.start()+start-1)].append(int(value))     # Appending number to star's dict value

total = 0
for numbers in stars.values():
    if len(numbers) == 2:                   # For * with excatly 2 adjacent numbers
        total += numbers[0] * numbers[1]

print("Result Part 2:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")