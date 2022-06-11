while True:
    try:
        answer = [0] * 4
        temp = input()
        for i in range(len(temp)):
            if temp[i].islower():
                answer[0] += 1
            elif temp[i].isupper():
                answer[1] += 1
            elif temp[i].isnumeric():
                answer[2] += 1
            elif temp[i].isspace():
                answer[3] += 1
        print(' '.join(map(str, answer)))
    
    except:
        break