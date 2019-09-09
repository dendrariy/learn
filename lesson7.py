x = input()
a = 'c'
b = 'g'
c = 'C'
d = 'G'
if a in x or b in x or c in x or d in x:
	p = ((x.count(a) + x.count(b)+ x.count(c) + x.count(d)) / len(x)) * 100
print (p)
