import timeit
import functools

start_t = timeit.default_timer()

# Recursive function that matches conditions with records
@functools.cache
def find_arrangements(record, conditions):
    result = 0
    if conditions == ():
        if '#' in record:
            return 0
        else:
            return 1
    if len(record) +1 < sum(conditions) + len(conditions):
        return 0
    if not '.' in record[0:conditions[0]]:
        if record[conditions[0]] != '#':
            if record[0] == '#':
                return find_arrangements(record[conditions[0]+1:].lstrip('.'), conditions[1:])
            else:
                result += find_arrangements(record[conditions[0]+1:].lstrip('.'), conditions[1:])
        else:
            if len(record) == conditions[0]:
                return 0
    else:
        if record[0] == '#':
            return 0
    if record[0] != '#':
        result += find_arrangements(record[1:].lstrip('.'), conditions)
        
    return result



with open('input.txt','r') as f:
    lines = f.readlines()

result_part_1 = 0
result_part_2 = 0
for line in lines:
    spring, conditions = line.split()
    conditions = list(map(int, conditions.split(',')))
    conditions_extended = conditions*5
    spring_extended = (spring + '?')*4 + spring + '.'
    spring += '.'
    result = find_arrangements(spring, tuple(conditions))
    result_part_1 += result
    result = find_arrangements(spring_extended, tuple(conditions_extended))
    result_part_2 += result

print("Result part 1: ", result_part_1)
print("Result part 2: ", result_part_2)

stop_t = timeit.default_timer()
print("in", '{:.3f}'.format(stop_t - start_t), "ms")