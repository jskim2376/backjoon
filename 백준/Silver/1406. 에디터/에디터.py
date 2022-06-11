import sys
editor_string = list(sys.stdin.readline())[:-1]
stack = []
count = int(sys.stdin.readline())
for _ in range(count):
    line = sys.stdin.readline()
    if line[0] == "L" and editor_string:
        stack.append(editor_string.pop())
    elif line[0] == "D" and stack:
            editor_string.append(stack.pop())
    elif line[0] == "B" and editor_string:
        editor_string.pop()
    elif line[0] == "P":
        editor_string.append(line[2])
editor_string.extend(reversed(stack))
print("".join(editor_string))