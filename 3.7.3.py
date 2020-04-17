n = int(input())
check = dict({'key':[]})
for i in range(n):
    word = str(input()).lower()
    check['key'].append(word)
m = int(input())
lst = []
for i in range(m):
    lst.append(str(input()).lower())
words = []
output = []
for i in range(len(lst)):
    words.append(lst[i].split())  
    for j in range(len(words[i])):
        if words[i][j] not in check['key']:
            output.append(words[i][j])
output = list(set(output))            
for i in range(len(output)):
    print(output[i])
    
