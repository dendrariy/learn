x = int(input())
s = []
for i in range(x+1):
    if len(s) <= x:
        for j in range (i):
            if len(s) < x:
                s.append(i)
for i in range(len(s)):
    print(s[i], end=" ")
