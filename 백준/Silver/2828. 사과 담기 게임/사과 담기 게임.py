N, M = map(int, input().split())
J = int(input())
count = 0
left, right = 1, M
apple = [int(input()) for i in range(J)]

for x in apple:
    if not (left<= x <=right):
        if left>x:
            count += left - x
            right-=(left - x)
            left = x
        else:
            count += x-right
            left+=(x-right)
            right = x
print(count)
        
        