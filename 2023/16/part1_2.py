import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    terrain = [list(row) for row in f.read().split('\n')]

size = len(terrain)

def run_path(steps):
    visited = set(steps)
    result = set()
    result.add(steps[0][:2])
    while steps:
        row, col, dir = steps.pop()
        symbol = terrain[row][col]
        
        if row > 0 and (row-1, col, '^') not in visited and (
            (dir == '^' and symbol in '|.') or
            (dir == '>' and symbol in '|/') or
            (dir == '<' and symbol in '|\\')):
            steps.append((row-1,col, '^'))
            visited.add((row-1, col, '^'))
            result.add((row-1, col))
        
        if row < size-1 and (row+1, col, 'v') not in visited and (
            (dir == 'v' and symbol in '|.') or
            (dir == '<' and symbol in '|/') or
            (dir == '>' and symbol in '|\\')):
            steps.append((row+1,col, 'v'))
            visited.add((row+1, col, 'v'))
            result.add((row+1, col))
        
        if col > 0 and (row, col-1, '<') not in visited and (
            (dir == '<' and symbol in '-.') or
            (dir == 'v' and symbol in '-/') or
            (dir == '^' and symbol in '-\\')):
            steps.append((row, col-1, '<'))
            visited.add((row, col-1, '<'))
            result.add((row, col-1))

        if col < size-1 and (row, col+1, '>') not in visited and (
            (dir == '>' and symbol in '-.') or
            (dir == '^' and symbol in '-/') or
            (dir == 'v' and symbol in '-\\')):
            steps.append((row, col+1, '>'))
            visited.add((row, col+1, '>'))
            result.add((row, col+1))

    return len(result)

result_part_1 = run_path([(0, 0, '>')])
print(result_part_1)

solutions = []
for i in range(size):
    solutions.append((0, i, 'v'))
    solutions.append((size-1, i, '^'))
    solutions.append((i, 0, '>'))
    solutions.append((i, size-1, '<'))

result_part_2 = max(run_path([start]) for start in solutions)
print(result_part_2)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")