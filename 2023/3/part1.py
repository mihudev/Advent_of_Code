import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    map = f.read()
width = re.match('.*\n', map).end()     # width = length of a single line

total = 0
for number in re.finditer('[0-9]+', map):   # Iterating over all numbers in map
    start, end, value = number.start(), number.end(), number.group()    # Coords for current number
    soroundings = map[start-1] + map[end] + map[start-width-1:end-width+1] + map[start+width-1:end+width+1]
    if re.findall('[^.\d]',soroundings):    # If anything else than '.' or number is found, increase the total
        total += int(value)

print("Result Part 1:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")