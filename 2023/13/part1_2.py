import timeit

start_t = timeit.default_timer()

with open('input.txt','r') as f:
    # Using 0's and 1's for easy conversion to int
    groups = f.read().replace('#', '1').replace('.', '0').split('\n\n')

# Finding solutions for part 1 by comparing left/top side with right/bottom
def find_row(pattern):
    for n in range(0, len(pattern)-1):
        if pattern[n] == pattern[n+1]:
            limit = min(n+1, len(pattern)-n-1)
            right = pattern[n+2 : n+limit+1]
            left = list(reversed(pattern[n-limit+1 : n]))
            if left == right:
                return n+1
    return 0

# Compare function for part 2, returns 1 if equal, 2 the numbers differ by 1 bit
def compare_bin(row1, row2):
    if row1 == row2:
        return 1
    if is_pow2(row1 ^ row2):
        return 2
    return 0

def is_pow2(number):
    return (number & (number - 1) == 0)

# Finding solutions for part 2
def find_row_smudge(pattern):
    for n in range(0, len(pattern) - 1):
        limit = min(n+1, len(pattern) - n - 1)          # Number of rows to check from top and bottom
        # x - index, diff - number of smudges, test - result of compare function
        x, diff, test = 0, 0, 1
        while diff < 2 and test > 0 and x < limit:
            test = compare_bin(pattern[n-x], pattern[n+x+1])
            diff += test//2
            x += 1
        if test != 0 and diff == 1 and x == limit:
            return n + 1
    return 0

result_part_1 = 0
result_part_2 = 0
for group in groups:
    pattern = [int(x, 2) for x in group.split('\n')]         #using a list of integers as main pattern data
    pattern_transposed = list(zip(*group.split('\n')))       #transposed pattern to be used for column search
    pattern_transposed = [int(x, 2) for x in [''.join(x) for x in pattern_transposed]]
    
    # Part 1
    # Searching for mirror row first, then column if no row is found
    result = find_row(pattern)
    if result == 0:
        result = find_row(pattern_transposed)
        result_part_1 += result
    else:
        result_part_1 += result * 100

    # Part 2
    result = find_row_smudge(pattern)
    if result == 0:
        result = find_row_smudge(pattern_transposed)
        result_part_2 += result
    else:
        result_part_2 += result * 100

print("Result Part 1:", result_part_1)
print("Result Part 2:", result_part_2)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")