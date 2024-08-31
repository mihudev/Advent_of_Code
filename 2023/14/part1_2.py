import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    terrain = [list(row) for row in f.read().split('\n')]
    terrain_transposed = list(zip(*terrain))      # Transposed 2D array for Part 1

length = len(terrain)
width = len(terrain[0])

# Load calculation for part 1
def calculate_load_part1(pattern):
    rock = length
    result = 0
    for x in range(0, length):
        if pattern[x] == '#':
            rock = length - x - 1
        elif pattern[x] == 'O':
            result += rock
            rock -= 1
    return result

def tilt_north():
    for x in range(0, width):
        rock = 0
        for y in range(0, length):
            if terrain[y][x] == '#':
                rock = y + 1
            elif terrain[y][x] == 'O':
                terrain[y][x] = '.'
                terrain[rock][x] = 'O'
                rock += 1

def tilt_west():
    for y in range(0, length):
        rock = 0
        for x in range(0, width):
            if terrain[y][x] == '#':
                rock = x + 1
            elif terrain[y][x] == 'O':
                terrain[y][x] = '.'
                terrain[y][rock] = 'O'
                rock += 1

def tilt_south():
    for x in range(0, width):
        rock = length - 1
        for y in range(length - 1, -1, -1):
            if terrain[y][x] == '#':
                rock = y - 1
            elif terrain[y][x] == 'O':
                terrain[y][x] = '.'
                terrain[rock][x] = 'O'
                rock -= 1

def tilt_east():
    for y in range(0, length):
        rock = width - 1
        for x in range(width - 1, -1, -1):
            if terrain[y][x] == '#':
                rock = x - 1
            elif terrain[y][x] == 'O':
                terrain[y][x] = '.'
                terrain[y][rock] = 'O'
                rock -= 1

# Load calculation for part 2
def calculate_load():
    result = 0
    for x in range(0, width):
        for y in range(0, length):
            if terrain[y][x] == 'O':
                result += length -y
    return result

# Confirming cycle by checking if the same pattern repeats directly after its first occurrence
def check_cycle():
    for n, number in enumerate(cycle):
        if number != cycles[cutoff+i+n]:
            return 0
    return len(cycle)

# Part 1
result_part_1 = 0
for pattern in terrain_transposed:
    result_part_1 += calculate_load_part1(pattern)

# cutoff is an arbitrary number determining how wide the search for a repeating cycle will be:
# cutoff * 2 = rounds of platform rolls that will be performed
# cutoff / 2 = maximum length of a repeating cycle
# cutoff = after skipping that many sequences search for a cycle will be started
cutoff = 200
cycles = []
for i in range(cutoff*2):
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()
    cycles.append(calculate_load())

cycle = []
cycle.append(cycles[cutoff])
cycle_length = 0
# Building cycle and checking it whenever a load value matching a cycle is found
for i in range(1, cutoff //2):
    if cycles[cutoff+i] == cycle[0] and cycle_length == 0:
        cycle_length = check_cycle()
    if cycle_length > 0:
        break
    # If solution is not found so far the cycle is extended by another load value
    cycle.append(cycles[cutoff+i])

final_cycle = (1_000_000_000 -cutoff) % cycle_length

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", cycle[final_cycle-1])

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")