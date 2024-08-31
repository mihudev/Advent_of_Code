import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    lines = f.readlines()

sequences = []
for line in lines:
    sequences.append([int(x) for x in line.strip().split(' ')])

result = 0
for sequence in sequences:
    i = 0
    while set(sequence) != {0}:                                 # Loop runs untill new sequence is all zeros
        result += sequence[0] if i % 2 == 0 else -sequence[0]   # Result is calculated by adding first values in odd sequences and subtracting even ones
        new_sequence = []
        for n in range(0, len(sequence) - 1):                   # Calculating new sequence
            new_sequence.append(sequence[n+1] - sequence[n])
        sequence = new_sequence
        i += 1

print("Result Part 2:", result)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")