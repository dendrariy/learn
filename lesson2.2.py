while 1:
    a = int(input())
    if a < 10:
        continue
    if 10 <= a <= 100:
        print(a)
    if a > 100:
        break
