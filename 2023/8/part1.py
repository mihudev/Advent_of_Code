import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

# Formatting L/R instructions to 0/1 int list
ins = [int(x) for x in lines[0].strip().replace('L', '0').replace('R', '1')]
# Nodes are kept as dict {node : next left, next right}
nodes = dict()
for line in lines[2:]:
    lhs, rhs = line.strip().split(' = ')
    nodes[lhs] = rhs.strip('()').split(', ')

current = 'AAA'
steps = 0
while current != 'ZZZ':                             # Loop stops once ZZZ is reached
    current = nodes[current][ins[steps%len(ins)]]   # i%len(ins) returns index for next L/R move within the instructions length
    steps += 1                                      # ins[i%len(ins)] returns L/R (0/1) depending on instructions
    
print("Result Part 1:", steps)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")