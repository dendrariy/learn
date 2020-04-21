n = int(input())
res = [[] for i in range(n)]
table = {}
for i in range(n):
    res[i] = str(input()).split(';')
    for j in range(len(res[i])):
        if res[i][j%2==0] not in table:
            table[res[i][j]] = [0,0,0,0,0]
for i in range(n):
    for j in range(len(res[i])):
        if res[i][j] in table:
            table[res[i][j]][0] += 1
            
for i in range(n):            
    if int(res[i][1]) > int(res[i][3]):
        table[res[i][0]][1] += 1
        table[res[i][2]][3] += 1
        table[res[i][0]][4] += 3
    elif int(res[i][1]) < int(res[i][3]):
        table[res[i][2]][1] += 1
        table[res[i][0]][3] += 1
        table[res[i][2]][4] += 3
    else:
        table[res[i][0]][2] += 1
        table[res[i][2]][2] += 1
        table[res[i][0]][4] += 1
        table[res[i][2]][4] += 1
    
for key, value in table.items():
    print(key+':', end='')
    print(*value, end='\n')

