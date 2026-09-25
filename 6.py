def sonlar(sn):
    yg = 0
    for x in sn:
        yg+=sn[x]
    return yg
lugat = {"a": 1, "b": 2, "c": 3}
print(sonlar(lugat))
