x = input()
i = 0
n = 1
s = str()
if n <= len(x):
	for i in range(1, len(x)):
		if x[i] == x[i-1]:
			n = n + 1
		if x[i] != x[i-1]:
			s += x[i-1] + str(n)
			n = 1
			while x[i] == x[i-1]:
				break
s += x[i] + str(n)
print (s)


