m = int(input())
answer = 0
for i in range(m):
    s = str(i)
    k=0
    for ss in s:
        k += int(ss)
    if m == i+k:
        answer = i
        break
print(answer)