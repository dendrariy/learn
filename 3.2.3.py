n = int(input())
x = 0
y = 0
res = dict()
for i in range(n):
    x = int(input())
    if x in res:
        print(res[x])
    else:
        y = f(x)
        res[x] = y
        print(res[x])
