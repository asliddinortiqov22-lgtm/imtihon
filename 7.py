def sonlar(son):
    yg = 1
    for x in  range(1, son, +1):
        yg += yg * x
    return yg
ns=int(5)
print(sonlar(ns))
