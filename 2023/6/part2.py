import math
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

time = float(lines[0].split(':')[1].replace(' ', ''))
distance = float(lines[1].split(':')[1].replace(' ', ''))

# Solving quadratic equation
d = time**2 - 4*distance
x1 = (time+math.sqrt(d))/2
x2 = (time-math.sqrt(d))/2
result = math.ceil(x1)-math.floor(x2)-1     # Finding number of integers within (x1, x2) range

print("Result Part 2:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")