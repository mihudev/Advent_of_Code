import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

total_score = 0
for line in lines:
    # Extracting numbers and dividing them into winning and held number sets
    line = line.strip().split(':')[1].split('|')
    win = set(int(x) for x in line[0].split())
    num = set(int(x) for x in line[1].split())
    # Using set intersection to generate a winning set and its length
    count = len(win.intersection(num))
    if count > 0:
        total_score += 2**(count-1)

print("Result Part 1:", total_score)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")