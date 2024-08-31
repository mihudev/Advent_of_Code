import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

sequences = []
for line in lines:
    sequences.append([int(x) for x in line.strip().split(' ')])

result = 0
for sequence in sequences:
    while set(sequence) != {0}:                                 # Loop runs untill new sequence is all zeros
        result += sequence[-1]                                  # For the final result it is enough to sum all last vlues from each sequence
        new_sequence = []
        for n in range(0, len(sequence) - 1):                   # Calculating new sequence
            new_sequence.append(sequence[n+1] - sequence[n])
        sequence = new_sequence

print("Result Part 1:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")