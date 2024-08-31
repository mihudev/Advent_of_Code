from bisect import bisect

space = []
with open('input.txt','r') as f:
    for line in f.readlines():
        space.append(list(x for x in line.rstrip()))

# Creating zipped space to easily check for empty columns
space_rotated = list(zip(*space))
length = len(space)
width = len(space[0])

rows = []
cols = []
# Checking empty rows
for y, row in enumerate(space):
    for n in range(width):
        if space[y][n] == '#':
            break
    else:
        rows.append(y)

# Checking empty columns
for x, col in enumerate(space_rotated):
    for n in range(length):
        if space_rotated[x][n] == '#':
            break
    else:
        cols.append(x)

galaxies = []
# Creating a list of all galaxies as (x, y) tuples
for y, row in enumerate(space):
    for x, point in enumerate(row):
        if space[y][x] == '#':
            galaxies.append((x, y))

result_part_1 = 0
result_part_2 = 0
# Calculating distance between galaxies for both parts
for start, start_galaxy in enumerate(galaxies):
    for end_galaxy in galaxies[start+1:]:
        distance = (abs(start_galaxy[0] - end_galaxy[0])
                          + abs(start_galaxy[1] - end_galaxy[1]))
        shift = (abs(bisect(cols, start_galaxy[0]) - bisect(cols, end_galaxy[0]))
                 + abs(bisect(rows, start_galaxy[1]) - bisect(rows, end_galaxy[1])))
        result_part_1 += distance + shift
        result_part_2 += distance + shift*999999

print("Result part 1:", result_part_1)
print("Result part 2:", result_part_2)