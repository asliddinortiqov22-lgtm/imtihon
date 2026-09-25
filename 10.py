def sonlar(a,b):
    yg = 0
    if a > 0:
        if b>0:
            yg = (a/b)
            return yg
        else:
            return "xatolik: 0 ga bolish mumkun emas"    
    else:
        return "xatolik: 0 ga bolish mumkun emas"    
        

c = 10
d = 0
print(sonlar(c, d))

