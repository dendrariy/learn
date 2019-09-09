x = input()
x1 = x.lower()
i = 0
n = 0
s = str()
m = str()
if n <= len(x):
	for i in range(0, len(x)):
		if x[i] == x[i-1]:
			n = n + 1
			s += x[i] + str(n)
		if x[i] != x[i-1]:
			m += s[-2:]
			n = 1
			s += x[i] + str(n)
			while x[i] == x[i-1]:
				break
m += s[-2:]
print (m)
