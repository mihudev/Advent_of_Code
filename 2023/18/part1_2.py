import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.read().split('\n')

# Directions for part 1 (RLUP) and part 2 (0123)
dirs = {
    'U': (-1,0),
    'R': (0,1),
    'D': (1,0),
    'L': (0,-1),
    '3': (-1,0),
    '0': (0,1),
    '1': (1,0),
    '2': (0,-1)
}

def solve(steps):
    perimeter = 0
    integral = 0
    segment = (0, 0)
    for step in steps:
        direction = step[0]
        length = step[1]
        perimeter += length
        point = (dirs[direction][0]*length, dirs[direction][1]*length)
        integral -= point[1]*segment[0]
        segment = (segment[0] + point[0], segment[1] + point[1])

    return perimeter + integral - perimeter//2 + 1

def part_1():
    steps = []
    for line in lines:
        step = line.split()
        steps.append((step[0], int(step[1])))

    return solve(steps)

def part_2():
    steps = []
    for line in lines:
        step = line.split()
        steps.append((step[2][-2], int(step[2][2:-2], 16)))

    return solve(steps)

print("Result Part 1: ", part_1())
print("Result Part 2: ", part_2())

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")