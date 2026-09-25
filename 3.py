def sonlar(son):
    count = 0
    for x in son:
        if x >= '0' and x <= '9':
            count+=1
    return count
qy = "abc123"     
print(sonlar(qy))   

