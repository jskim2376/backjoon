count = int(input())
lines = []
for _ in range(count):
    lines.append(input())

for line in lines:
    left_ps = 0
    for l in line:
        if l == '(':
            left_ps+=1
        elif left_ps>0:
            left_ps-=1
        else:
            left_ps=1
            break
    if left_ps != 0:
        print("NO")
    else:
        print("YES")