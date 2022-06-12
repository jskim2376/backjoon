import sys
line = sys.stdin.readline()[:-1]

stack = []
result = 0
for i in range(len(line)):
    if line[i]=="(":
        stack.append('(')
    elif line[i]==")":
        stack.pop()
        if line[i-1]==")":
            result+=1
        else:
            result+=len(stack)
print(result)        
