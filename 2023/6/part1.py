import re
import math
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

times = [float(x) for x in re.findall('\d+', lines[0])]
distances = [float(x) for x in  re.findall('\d+', lines[1])]

# Solving quadratic equation
result = 1
for race in zip(times, distances):
    d = race[0]**2 - 4*race[1]
    x1 = (race[0]+math.sqrt(d))/2
    x2 = (race[0]-math.sqrt(d))/2
    result *= math.ceil(x1)-math.floor(x2)-1    # Finding number of integers within (x1, x2) range

print("Result Part 1:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")