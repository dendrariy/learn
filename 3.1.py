def f(x):
    res = 0
    if x <= -2:
        res = 1 - (x + 2)**2
    if -2 < x < 2:
        res = -(x/2)
    if x > 2:
        res = (x-2)**2 + 1
    return res