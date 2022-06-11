count = int(input())
words = []
for _ in range(count):
    words.append(input())

for word in words:
    line = []
    for w in word.split():
        line.append(w[::-1])
    print(" ".join(line))