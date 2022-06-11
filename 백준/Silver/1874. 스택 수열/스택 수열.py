def solution(lines):
    current_num = 1
    stack = [0]
    result = []
    for line in lines:
        while stack[-1] < line:
            stack.append(current_num)
            result.append('+')
            current_num+=1
        if stack[-1] == line:
            stack.pop()
            result.append('-')
        else:
            print("NO")
            return False
    
    for r in result:
        print(r)

count = int(input())
lines = []
for _ in range(count):
    lines.append(int(input()))
    
solution(lines)
