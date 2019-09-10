a = [int(i) for i in input().split()]
a.sort()
b = a
s = []
n = 0
for i in range (len(b)):
        if len(b) > 1:
                if b[i] == b[i-1]:
                  n += 1
                  if n > 0:
                      s.append(b[i])
for i in range(len(s)):
        print(s[i], end=" ")