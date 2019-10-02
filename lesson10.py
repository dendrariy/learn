a = [int(i) for i in input().split()]
a.sort()
b = a
s = []
x = []
for i in range (len(b)):
        if len(b) > 1:
                if b[i] == b[i-1]:
                      s.append(b[i])
x = list(set(s))
for i in range(len(x)):
        print(x[i], end=" ")