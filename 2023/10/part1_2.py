

with open('input.txt','r') as f:
    terrain = f.readlines()

# For each direction - coordinates to check with their matching symbols
dirs = {
    'F' : [(1, 0, 'LJ|S'), (0, 1, '7J-S')],
    '7' : [(0,-1, 'FL-S'), (1, 0, 'LJ|S')],
    'L' : [(-1,0, 'F7|S'), (0, 1, '7J-S')],
    'J' : [(-1,0, 'F7|S'), (0,-1, 'FL-S')],
    '|' : [(-1,0, 'F7|S'), (1, 0, 'LJ|S')],
    '-' : [(0,-1, 'FL-S'), (0, 1, '7J-S')],
    'S' : [(1, 0, 'LJ|S'), (0, 1, '7J-S'), (-1,0, 'F7|S'), (0,-1, 'FL-S')],
    '.' : []
}

# Symbols for a new map in part 2
mapping = {
    'J' : '^',
    'L' : '^',
    '7' : 'v',
    'F' : 'v',
    '|' : '|',
    '-' : '-',
    'S' : 'S'
}

# Finding start of the loop
for n, line in enumerate(terrain):
    if line.find('S') > -1:
        start = (n, line.find('S'))
        break
current_sign = 'S'

width = len(terrain[0]) - 1
length = len(terrain)

# Generating an empty map to be populated by loop symbols
terrain_mapped = [['.'] * width for i in range(length)]
terrain_mapped[start[0]][start[1]] = 'S'
current = start
prev = (length + 1, width +1)

result_part_1 = 0
# Looking for next node for each step in the loop until the start is reached
while next != start:
    for dir in dirs[current_sign]:
        next = (dir[0] + current[0], dir[1] + current[1])
        if terrain[next[0]][next[1]] in dir[2] and prev != next:
            terrain_mapped[next[0]][next[1]] = mapping[terrain[next[0]][next[1]]]
            prev = current
            current_sign = terrain[next[0]][next[1]]
            current = next
            break
    result_part_1 += 1

print("Result Part 1: ", result_part_1 // 2)

result_part_2 = 0
# Checking all symbols from left to right and conditions for a point to be within the loop:
# -sum of F and 7 (v) symbols and L and J (^) symbols must be even and pipes odd
# -sum of F and 7 (v) symbols and L and J (^) symbols must be odd and pipes even
for n, line in enumerate(terrain_mapped):
    pipe, up, down = 0, 0, 0
    for x in range(width - 1):
        match terrain_mapped[n][x]:
            case '|':
                pipe += 1
            case '^':
                up += 1
            case 'v':
                down += 1
            case 'S':
                pipe += 1
            case '.':
                if (up % 2 == 0) and (down % 2 == 0) and pipe % 2 == 1:
                    terrain_mapped[n][x] = 'X'
                    result_part_2 += 1
                if ((up % 2 == 1) or (down % 2 == 1)) and pipe % 2 == 0:
                    terrain_mapped[n][x] = 'X'
                    result_part_2 += 1

print("Result Part 2: ", result_part_2)