def sonlar(son):
    yangi = []
    for x in son:
        if x <0:
            yangi += [x*-1]
        else:
            yangi += [x]   
    return yangi
sn = [-3, 2, -1]
print(sonlar(sn))        