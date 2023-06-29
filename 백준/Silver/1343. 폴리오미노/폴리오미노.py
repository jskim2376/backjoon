board = input()
count = 0
text = ""
for i in range(len(board)):
    if board[i] == 'X':
        count+=1
    if board[i] == '.' or i==len(board)-1:
        if count != 0:
            if count%2 == 1:
                text = -1
                break
            for j in range(count//4):
                text = text + "AAAA"
            if count%4 == 2:
                text = text + "BB"
            count=0
        if board[i] == '.':
            text = text + "."
print(text)