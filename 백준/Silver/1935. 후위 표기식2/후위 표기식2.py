import sys
count = int(sys.stdin.readline())
line = sys.stdin.readline()[:-1]
values = [sys.stdin.readline()[:-1] for i in range(count)]

stack = []
for l in list(line):
    if l in ["+", "-", "*", "/"]:
        right_op = stack.pop()
        left_op = stack.pop()
        stack.append(str(eval(left_op+l+right_op))) 
    else:
        stack.append(str(values[ord(l)-65]))
print(f"{float(stack[0]):.2f}")