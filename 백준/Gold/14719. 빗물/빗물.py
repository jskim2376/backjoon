import sys
map_size = list(map(int, sys.stdin.readline()[:-1].split()))
block = list(map(int, sys.stdin.readline()[:-1].split()))

volume = 0
left, right= 0, len(block)-1
left_max, right_max = block[left], block[right]
while left < right:
    left_max, right_max = max(block[left], left_max), max(block[right], right_max)
    if left_max <= right_max:
        volume+= left_max-block[left]
        left += 1
    else:
        volume+= right_max-block[right]
        right -=1


print(volume)