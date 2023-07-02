def snow(data, dwarf,depth):
    if depth==0:
        if sum(data) == 100:
            data.sort()
            for d in data:
                print(d)
            exit(0)
        return
    for i in range(len(dwarf)):
        snow(data + [dwarf[i]], dwarf[:i] + dwarf[i+1:], depth-1)
        
dwarf = []
for i in range(9):
    dwarf.append(int(input()))

snow([],dwarf, 7)