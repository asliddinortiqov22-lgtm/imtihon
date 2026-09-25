def qosh(son):
    jami = 0
    for x in son:
        if x > 0:
            jami += x
    return jami 
c = [1,-2,3,-4,5]
print(qosh(c))       
