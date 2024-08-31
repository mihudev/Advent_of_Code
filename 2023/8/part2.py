from math import lcm
import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# Formatting L/R instructions to 0/1 int list
ins = [int(x) for x in lines[0].strip().replace('L', '0').replace('R', '1')]

# current is a list of all seprte chains starting at '..A' nodes
current = []
nodes = dict()
for line in lines[2:]:
    lhs, rhs = line.strip().split(' = ')        # Nodes are kept as dict {node : next left, next right}
    nodes[lhs] = rhs.strip('()').split(', ')
    if lhs[2] == 'A':                           # If node ends with 'A', add it to the starting list (current)
        current.append(lhs)

steps = 0
state = [0] * len(current)                      # State is used as a loop condition and final result
while 0 in state:                               # As long as the list is not populated with non-zero values, the loop will continue
    for n, x in enumerate(current):             # Each node in current is substituted with its next step
        current[n] = nodes[x][ins[steps%len(ins)]]
        if current[n][2] == 'Z' and state[n] == 0:
            state[n] = int(steps+1)             # If a node ending with 'Z' is reached for the first time, 
    steps += 1

print("Result Part 2:", lcm(*state))                              # Result can be easily calculated by least common multiple, which gives the step in which loops end at 'Z' for all starting nodes
stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")