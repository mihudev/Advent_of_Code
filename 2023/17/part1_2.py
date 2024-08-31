import timeit
from heapq import heappop, heappush

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    terrain = [list(int(x) for x in row) for row in f.read().split('\n')]

size = len(terrain)

# Using heapq for easy access to elements with the lowest heat loss
def part_1():
    # Node queue element: heat loss, row, column, steps in current direction, row direction, col direction
    nodes = [(0,0,0,0,0,0)]
    visited = set()

    while nodes:
        heat, row, col, steps, rd, cd = heappop(nodes)
        
        if row == size -1 and col == size -1:       # Break if the end is reached
            break
        if (row, col, steps, rd, cd) in visited:    # Skip node if it was already evaluated
            continue
        visited.add((row, col, steps, rd, cd))      # Adding node to a set of visited nodes

        # Directions represented as coordinates deltas
        # rd - row direction, cd - column direction
        for new_rd, new_cd in ((-1,0),(0,1),(1,0),(0,-1)):
            new_row = row + new_rd
            new_col = col + new_cd

            # Node is skipped if new row or column is out of bounds
            if new_row < 0 or new_row == size or new_col < 0 or new_col == size or (new_rd == -rd and new_cd == -cd):
                continue

            new_steps = 1                       # Step count is set to 1 for nodes left of right from original direction
            if new_rd == rd and new_cd == cd:   # Condition for moving forward in the original direction
                if steps > 2:                   # Move forward is skipped if already 3 steps were made in this direction
                    continue
                else:
                    new_steps = steps+1        # Step counter increased for moving forward

            # Adding next node to the heap with heat increased by heat loss value
            heappush(nodes, (heat + terrain[new_row][new_col], new_row, new_col, new_steps, new_rd, new_cd))

    return heat

def part_2():
    # Node queue element: heat loss, row, column, steps in current direction, row direction, col direction
    # part 2 requires specified direction since it is not possible to turn until 4 steps are made
    nodes = [(0,0,0,0,1,0), (0,0,0,0,0,1)]
    visited = set()

    while nodes:
        heat, row, col, steps, rd, cd = heappop(nodes)

        if row == size-1 and col == size-1:
            break
        if (row, col, steps, rd, cd) in visited:
            continue
        visited.add((row, col, steps, rd, cd))

        for new_rd, new_cd in ((-1,0),(0,1),(1,0),(0,-1)):
            new_row = row + new_rd
            new_col = col + new_cd
            if new_row < 0 or new_row == size or new_col < 0 or new_col == size or (new_rd == -rd and new_cd == -cd):
                continue
            if new_rd == rd and new_cd == cd:
                if steps > 9:   # Step limit increased for part 2
                    continue
                else:
                    new_steps = steps+1
            else:
                if steps < 4:   # Minimum steps before direction change is possible
                    continue
                else:
                    new_steps = 1

            heappush(nodes, (heat + terrain[new_row][new_col], new_row, new_col, new_steps, new_rd, new_cd))

    return heat

print("Result part 1:", part_1())
print("Result part 2:", part_2())

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")