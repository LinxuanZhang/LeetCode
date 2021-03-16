def reverse(x):
    if x >= 0:
        res = int(str(x)[::-1])
    else:
        res = -int(str(-x)[::-1])
    if res > (1<<31)-1 or res < -(1<<31):
        res = 0
    return res
