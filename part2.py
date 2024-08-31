import re
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# Appended letters to digits because of overlapping numbers
Digits = [
    ("one", "o1e"),
    ("two", "t2o"),
    ("three", "t3e"),
    ("four", "f4r"),
    ("five", "f5e"),
    ("six", "s6x"),
    ("seven", "s7n"),
    ("eight", "e8t"),
    ("nine", "n9e"),
]

total = 0
for line in lines:
    for word, digit in Digits:
        line = line.replace(word, digit)
    numbers = re.findall(r'[\d]',line)
    total += int(numbers[0] + numbers[-1])
print("Result Part 2:", total)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")