with open('input.txt','r') as f:
    codes = f.readline().split(',')

results = []
for code in codes:
    value = 0
    for symbol in code:
        value = ((value + ord(symbol)) * 17) % 256
    results.append(value)

print("Result Part 1:", sum(results))