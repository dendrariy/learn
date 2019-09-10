lst = [int(i) for i in input().split()]
x = int(input())
s = []
for i in range(len(lst)):
    if lst[i] == x:
        s.append(i)
if len(s) > 0:
    s.sort()
    out = s
    for i in range(len(out)):
     print(out[i], end=" ")
if len(s) == 0:     
    print ("Отсутствует")