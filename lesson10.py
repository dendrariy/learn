a = [int(i) for i in input().split()]
a.sort()
b = a
s = [0 for i in range(len(a))]
i = 0
x = []
for j in range (len(a)):
       if b[j] == b[j-1]:
               s[i] = b[j]
       if b[j] != b[j-1]:
               i += 1
               s[i] = b[j]
               while b[j] == b[j-1]:
                       break
for i in range (len(s)):
       if s[i] != 0:
               x.append(s[i])
       if s[i] == 0:
               x.insert(0, '0')
for i in range (len(x)):
       print (x[i], end=" ")