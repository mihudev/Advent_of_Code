import re
import timeit

start_t = timeit.default_timer()
with open('input.txt','r') as f:
    lines = f.readlines()


total = 0
for line in lines:
    numbers = re.findall(r'[\d]',line)
    total += int(numbers[0] + numbers[-1])
print("Result Part 1:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")