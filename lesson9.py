a = [int(i) for i in input().split()]
b = [0 for i in range(len(a))]
for j in range (len(a)):
	if len(a) == 1:
        	print (a[j], end=" ")
	elif j < len(a) - 1:
		b[j] = a[j-1] + a[j+1]
	elif j == len(a) - 1:
		b[j] = a[j-1] + a[0]
for j in range (len(a)):
	if len(a) != 1:
	print (b[j], end=" ")
