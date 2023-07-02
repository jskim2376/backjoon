start, end = map(int, input().split())
sequence = [0]
for i in range(1000+1):
    for j in range(i):
        sequence.append(i)
print(sum(sequence[start:end+1]))