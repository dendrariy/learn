inp = str(input())
line = inp.lower()
lst = line.split()
d = dict()
value = 1
for i in range(len(lst)):
    if lst[i] in d:
        d[lst[i]] += 1
    else:
        d[lst[i]] = value
for lst[i] in d:
    print(lst[i], d[lst[i]])
    
