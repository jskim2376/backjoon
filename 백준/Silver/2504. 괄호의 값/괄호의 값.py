import sys
brackets = sys.stdin.readline()[:-1]
open_bracket = {']':'[', ')':'('}
bnum = {']':3, ')':2}
stack = []

# Check Bracket
for bracket in brackets:
    if bracket in ['(', '[']:                #여는 괄호는 스택에 추가
        stack.append(bracket)
    else:
        if stack and stack[-1] == open_bracket[bracket]:
            stack.pop(-1)
        else:
            print(0)
            exit(0)

if stack:
    print(0)
    exit(0)

stack = []
def compress(stack, close_bracket):
    number = stack.pop()
    while type(stack[-1]) == int:
        number += stack.pop()
    stack.pop()
    stack.append(number*bnum[close_bracket])

for bracket in brackets:
    if bracket in ['(', '[']:                #여는 괄호는 스택에 추가
        stack.append(bracket)
    elif stack[-1] == open_bracket[bracket]: #바로 닫히는 괄호는 값을 스택에 추가
        stack.pop()
        stack.append(bnum[bracket])
    elif type(stack[-1]) == int:
        compress(stack, bracket)            #괄호사이에 숫자들이 있으면 모두 더하고 닫히는 괄호의 값을 곱함 
print(sum(stack))
