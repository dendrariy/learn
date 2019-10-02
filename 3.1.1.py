l = [int(i) for i in input().split()]
s = []
for i in range(len(l)):
    if l[i] % 2 == 0:
        s.append(l[i] // 2)
l.clear()
for i in range(len(s)):
    l.append(s[i])
print(l)
