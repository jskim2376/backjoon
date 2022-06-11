import sys
line = sys.stdin.readline()[:-1]

i=0
result = 0
stack = []
while i<len(line):
    if i+1<len(line) and line[i]=="(" and line[i+1]==")":
        result+=len(stack)
        i+=2
    elif line[i]=="(":
        stack.append('(')
        i+=1
    elif line[i]==")":
        stack.pop()
        i+=1
        result+=1
print(result)        
