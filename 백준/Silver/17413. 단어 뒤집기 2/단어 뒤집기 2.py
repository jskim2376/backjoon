import sys
line = sys.stdin.readline()[:-1]
result = []
i=0
while i<len(line):
    if line[i] == "<":
        while line[i]!=">":
            result.append(line[i])
            i+=1
        result.append(line[i])
        i+=1
    elif line[i] == " ": 
        result.append(line[i])
        i+=1
    else:
        stack = []
        while i<len(line) and line[i]!=" " and line[i]!="<":
            stack.append(line[i])
            i+=1
        result.extend(reversed(stack))
print("".join(result))        