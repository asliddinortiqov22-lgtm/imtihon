def sonlar(son):
    manfiy = []
    for x in son:
        if x < 0:
            manfiy += [x]
    return manfiy
kirish = [3, -1, 0, -7]
print(sonlar(kirish))        