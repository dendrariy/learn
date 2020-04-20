n = int(input())

res = [[0 for j in range(n)] for i in range(n)]

i = 0
j = 0
r = 1
for j in range(n):
    res[i][j] = r
    r += 1
    if res[i][-1] != 0:
        j = n - 1
        for i in range(1, n):
            res[i][j] = r
            r += 1
            if res[-1][-1] != 0:
                i = n - 1
                for j in range(2, n + 1):
                    res[i][-j] = r
                    r += 1
                    if res[-1][0] != 0:
                        j = 0
                        for i in range(2, n):
                            res[-i][j] = r
                            r += 1
                            if res[1][0] != 0:
                                i = 1
                                for j in range(1, n - 1):
                                    res[i][j] = r
                                    r += 1
                                    if res[1][3] != 0:
                                        j = 3
                                        for i in range(2, n - 1):
                                            res[i][j] = r
                                            r += 1
                                            if res[3][3] != 0:
                                                i = 3
                                                for j in range(3, n):
                                                    res[i][-j] = r
                                                    r += 1
                                                    if res[3][1] != 0:
                                                        i = 2
                                                        for j in range(1, n - 2):
                                                            res[i][j] = r
                                                            r += 1                                         

for i in range (n):
    print(res[i])
